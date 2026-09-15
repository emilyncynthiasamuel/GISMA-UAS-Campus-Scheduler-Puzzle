def validate_schedule(classes, rooms, holidays):
    errors = []
    room_map = {r.room_id: r for r in rooms}
    holiday_dates = {h["date"] for h in holidays}

    weekday_map = {
        "Monday": "2026-09-14",
        "Tuesday": "2026-09-15",
        "Wednesday": "2026-09-16",
        "Thursday": "2026-09-17",
        "Friday": "2026-09-18"}
    for c in classes:
        if c.room_id not in room_map:
            errors.append(f"{c.class_id} ({c.module_code}): Room {c.room_id} is not found.!")
            continue
        room = room_map[c.room_id]
        if c.student_count > room.capacity:
            errors.append(f"{c.class_id}: Room Capacity Exceeded.")
        if room.campus_id != c.campus_id:
            errors.append(f"{c.class_id}: Campus Mismatch.")
        date = weekday_map.get(c.day)
        if date in holiday_dates:
            errors.append(f"{c.class_id}: Scheduled on Public Holiday ({date}).")
    for i in range(len(classes)):
        for j in range(i + 1, len(classes)):
            a = classes[i]
            b = classes[j]
            if a.day == b.day and a.time_slot == b.time_slot:
                if a.room_id == b.room_id:
                    errors.append(f"Room Clash: {a.class_id} & {b.class_id}")
                if a.professor_id == b.professor_id:
                    errors.append(f"Professor Clash: {a.professor_id}")
                if a.group_id == b.group_id:
                    errors.append(f"Student Group Clash: {a.group_id}")
    return errors