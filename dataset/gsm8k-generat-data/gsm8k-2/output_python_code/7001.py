def solution():
    """Liz roasts 2 16 pounds turkeys every Thanksgiving. She can only roast them 1 at a time because she has a small oven. She roasts each turkey for 15 minutes per pound. If dinner is served at 6:00 pm what is the latest time she can start roasting the turkeys?"""
    turkey_weight = 16
    turkey_cooking_time = turkey_weight * 15
    total_cooking_time = turkey_cooking_time * 2
    latest_start_time = datetime.time(18, 0) - datetime.timedelta(minutes=total_cooking_time)
    result = latest_start_time
    return result

print(solution())