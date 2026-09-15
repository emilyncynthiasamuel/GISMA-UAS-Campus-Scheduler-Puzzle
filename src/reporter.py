import csv
from pathlib import Path
def create_all_reports(classes, waste, errors):
    out_dir = Path(__file__).parent.parent / "output"
    out_dir.mkdir(exist_ok=True)
    csv_path = out_dir / "timetable.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Class ID", "Module Code", "Module Name", "Student Group", 
            "Section", "Professor ID", "Day", "Time Slot", "Room ID", "Campus", "Student Count"])
        for c in classes:
            writer.writerow([
                c.class_id, c.module_code, c.module_name, c.group_id,
                c.section, c.professor_id, c.day, c.time_slot,
                c.room_id, c.campus_id, c.student_count])
    conflict_path = out_dir / "conflict_report.txt"
    with open(conflict_path, "w", encoding="utf-8") as f:
        f.write("GISMA UNIVERSITY OF APPLIED SCIENCES - CAMPUS SCHEDULER PUZZLE'S CONFLICT REPORT\n")
        f.write("-" * 70 + "\n\n")
        if errors:
            for err in errors:
                f.write(f"- {err}\n")
        else:
            f.write("Hello Cynthia! No Hard Constraint Conflicts or Duplicate Bookings were detected.\n")
    summary_path = out_dir / "scheduling_report.txt"
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write("GISMA UNIVERSITY OF APPLIED SCIENCES - THE SCHEDULING REPORT\n")
        f.write("-" * 60 + "\n\n")
        f.write(f"Student: Cynthia Samuel (Master of Engineering - Computer Science)\n")
        f.write(f"Scheduled Classes: {len(classes)}\n")
        f.write(f"Total Room Capacity Waste: {waste} Seat Slots\n")
        f.write(f"Validation Conflicts Flagged: {len(errors)}\n")