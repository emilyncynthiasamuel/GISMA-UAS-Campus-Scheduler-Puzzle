from data_loader import load_project_objects
from greedy_solver import build_class_requests, greedy_schedule
from graph_engine import graph_schedule
from optimizer import optimize_rooms
from backtracker import recover_schedule
from validator import validate_schedule
from reporter import create_all_reports
def main():
    print("Initializing GISMA University Campus Puzzle Scheduler...Please Wait, Cynthia!")
    data, modules, groups, students, rooms, teaching, professors, holidays, rules = load_project_objects()
    split_threshold = rules.get("group_split_threshold", 45)
    requests = build_class_requests(modules, groups, students, split_threshold)
    requests = graph_schedule(requests, teaching)
    scheduled, unscheduled_pool = greedy_schedule(
        requests,
        rooms,
        [],
        professors,
        teaching
    )
    scheduled, unscheduled_pool = recover_schedule(unscheduled_pool, scheduled, rooms, professors, teaching)
    scheduled, total_waste = optimize_rooms(scheduled, rooms)
    errors = validate_schedule(scheduled, rooms, holidays)
    create_all_reports(scheduled, total_waste, errors)
    print("\n" + "-" * 50)
    print("GISMA UAS CAMPUS SCHEDULER PUZZLE - EXECUTION OUTPUT SUMMARY")
    print("-" * 50)
    print(f"Scheduled Classes       : {len(scheduled)}")
    print(f"Unscheduled Classes     : {len(unscheduled_pool)}")
    print(f"Room Capacity Waste     : {total_waste} seats")
    print(f"Validation Conflicts    : {len(errors)}")
    print("\nAll the CSV and Text Reports are successfully generated in the /output folder!")
if __name__ == "__main__":
    main()