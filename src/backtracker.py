from models import ScheduledClass
def is_valid(req, day, slot, room, scheduled):
    if room.campus_id != req["campus"]:
        return False
    if room.capacity < req["count"]:
        return False
    for c in scheduled:
        if c.day == day and c.time_slot == slot:
            if c.room_id == room.room_id:
                return False
            if c.professor_id == req["professor"]:
                return False
            if c.group_id == req["group"]:
                return False
    return True
def backtrack(pos, pool, scheduled, rooms, days, slots):
    if pos >= len(pool):
        return True
    req = pool[pos]
    for day in days:
        for slot in slots:
            for room in rooms:
                if not is_valid(req, day, slot, room, scheduled):
                    continue
                new = ScheduledClass(f"GISMA-REC-{len(scheduled)+1}", req["code"], req["name"], req["group"], req["professor"], day, slot, room.room_id, req["campus"], req["count"], req["ids"], req["sec"])
                scheduled.append(new)
                if backtrack(pos + 1, pool, scheduled, rooms, days, slots):
                    return True
                scheduled.pop()
    return False
def recover_schedule(pool, scheduled, rooms, professor_data, teaching):
    if len(pool) == 0:
        return scheduled, pool
    days = teaching["days"]
    slots = teaching["standard_slots"]
    pool.sort(key=lambda x: x["count"], reverse=True)
    remaining = []
    for req in pool:
        temp = [req]
        ok = backtrack(0, temp, scheduled, rooms, days, slots)
        if not ok:
            remaining.append(req)
    return scheduled, remaining