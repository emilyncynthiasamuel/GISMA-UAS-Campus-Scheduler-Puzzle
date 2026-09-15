from models import ScheduledClass
def check_time_overlap(slot1, slot2):
    try:
        start1, end1 = slot1.split("-")
        start2, end2 = slot2.split("-")
        return start1 < end2 and start2 < end1
    except Exception:
        return slot1 == slot2
def build_class_requests(modules, groups, students, split_threshold):
    requests = []
    for group in groups:
        for code in group.modules:
            module = next((m for m in modules if m.code == code), None)
            if not module:
                continue
            active_students = [s.student_id
                for s in students
                if s.group_id == group.group_id
                and code not in s.completed_modules]
            count = len(active_students)
            if count == 0:
                count = module.students
            if count >= split_threshold:
                half = count // 2
                requests.append({**vars(module), "group": group.group_id, "count": half, "ids": active_students[:half], "sec": "A"})
                requests.append({**vars(module), "group": group.group_id, "count": count - half, "ids": active_students[half:], "sec": "B"})
            else:
                requests.append({**vars(module), "group": group.group_id, "count": count, "ids": active_students, "sec": ""})
    return requests
def professor_available(professor_id, day, slot, professors):
    current = f"{day} {slot}"
    for p in professors:
        if p["professor_id"] == professor_id:
            if current in p.get("avoid_slots", []):
                return False
    return True
def greedy_schedule(requests, rooms, schedule, professors, teaching_config):
    requests.sort(key=lambda x: x["count"], reverse=True)
    days = teaching_config["days"]
    slots = teaching_config["standard_slots"]
    for req in requests:
        placed = False
        for day in days:
            if placed:
                break
            for slot in slots:
                if placed:
                    break
                if not professor_available(req["professor"], day, slot, professors):
                    continue
                for room in rooms:
                    if room.campus_id != req["campus"]:
                        continue
                    if room.capacity < req["count"]:
                        continue
                    conflict = False
                    for existing in schedule:
                        if (existing.day == day
                            and check_time_overlap(existing.time_slot, slot)):
                            if (existing.room_id == room.room_id
                                or existing.professor_id == req["professor"]
                                or existing.group_id == req["group"]):
                                conflict = True
                                break
                    if conflict:
                        continue
                    class_id = f"GISMA-{len(schedule)+101}"
                    schedule.append(
                        ScheduledClass(class_id, req["code"], req["name"], req["group"], req["professor"], day, slot, room.room_id, req["campus"], req["count"], req["ids"], req["sec"]))
                    placed = True
                    break
    unscheduled = []
    for req in requests:
        found = False
        for c in schedule:
            if (c.module_code == req["code"]
                and c.group_id == req["group"]
                and c.section == req["sec"]):
                found = True
                break
        if not found:
            unscheduled.append(req)
    return schedule, unscheduled