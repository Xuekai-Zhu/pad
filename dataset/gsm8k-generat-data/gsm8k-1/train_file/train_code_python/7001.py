def solution():
    """Liz roasts 2 16 pounds turkeys every Thanksgiving. She can only roast them 1 at a time because she has a small oven. She roasts each turkey for 15 minutes per pound. If dinner is served at 6:00 pm what is the latest time she can start roasting the turkeys?"""
    turkey_weight = 16
    num_turkeys = 2
    time_per_pound = 15  # minutes
    total_time = turkey_weight * time_per_pound * num_turkeys
    latest_start_time = "3:45 pm"
    return latest_start_time

print(solution())