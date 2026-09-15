class Room:
    def __init__(self, room_id, capacity, room_type, campus_id):
        self.room_id = room_id
        self.capacity = capacity
        self.room_type = room_type
        self.campus_id = campus_id  
    def __repr__(self):
        return f"<Room {self.room_id} | Cap: {self.capacity} | Campus: {self.campus_id}>"
class Module:
    def __init__(self, code, name, students, professor, campus):
        self.code = code
        self.name = name
        self.students = students
        self.professor = professor
        self.campus = campus
class StudentGroup:
    def __init__(self, group_id, programme, intake, modules):
        self.group_id = group_id      
        self.programme = programme    
        self.intake = intake          
        self.modules = modules        
class Student:
    def __init__(self, student_id, group_id, completed_modules):
        self.student_id = student_id
        self.group_id = group_id
        self.completed_modules = completed_modules  
class ScheduledClass:
    def __init__(self, cid, code, name, group, prof, day, slot, room, campus, students, ids, section=""):
        self.class_id = cid
        self.module_code = code
        self.module_name = name
        self.group_id = group
        self.professor_id = prof
        self.day = day
        self.time_slot = slot       
        self.room_id = room
        self.campus_id = campus
        self.student_count = students
        self.student_ids = ids      
        self.section = section      