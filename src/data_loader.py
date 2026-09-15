import json
from pathlib import Path
from models import Room, Module, StudentGroup, Student
def load_project_objects():
    path = Path("data/constraints.json")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    rooms = []
    for campus in data.get("campuses", []):
        campus_id = campus["id"]
        for room in campus.get("rooms", []):
            rooms.append(Room(room_id=room["id"], capacity=room["capacity"],
                    room_type=room.get("room_type", "Lecture Room"), campus_id=campus_id))
    modules = []
    for m in data.get("modules", []):
        modules.append(
            Module(m["code"], m["name"], m["students"], m["professor"], m["campus"]))
    groups = []
    for g in data.get("student_groups", []):
        groups.append(StudentGroup(g["group_id"], g.get("programme", "Unknown"), g.get("intake", "October"), g.get("modules", [])))
    students = []
    counter = 1
    for group in groups:
        size = 0
        for module in modules:
            if module.code in group.modules:
                size = max(size, module.students)
        if size == 0:
            size = 25
        for i in range(size):
            completed = []
            if group.group_id == "M501A" and i == 0:
                completed = ["M501"]
            students.append(Student(f"STU{counter:04}", group.group_id, completed))
            counter += 1
    return (data, modules, groups, students, rooms,
        data.get("teaching_schedule", {}), data.get("professor_constraints", []),
        data.get("public_holidays", []), data.get("scheduling_constraints", {"group_split_threshold": 40}))