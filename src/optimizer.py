def optimize_rooms(classes, rooms):
    total_waste = 0
    for c in classes:
        best_room = None
        min_waste_for_class = float('inf')
        for room in rooms:
            if room.campus_id != c.campus_id or room.capacity < c.student_count:
                continue
            room_in_use = any( other != c and other.day == c.day and 
             other.time_slot == c.time_slot and other.room_id == room.room_id
                  for other in classes)
            if room_in_use:
                continue
            waste = room.capacity - c.student_count
            if waste < min_waste_for_class:
                min_waste_for_class = waste
                best_room = room
        if best_room:
            c.room_id = best_room.room_id
            total_waste += min_waste_for_class
    return classes, total_waste