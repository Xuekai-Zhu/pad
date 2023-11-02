def solution():
    """Jasmine gets off of work at 4:00 pm. After that, it will take her 30 minutes to commute home, 30 minutes to grocery shop, 10 minutes to pick up the dry cleaning, 20 minutes to pick up the dog from the groomers and 90 minutes to cook dinner when she returns home. What time will she eat dinner?"""
    start_time = 4 * 60  # convert start time to minutes
    commute_time = 30
    grocery_time = 30
    dry_cleaning_time = 10
    groomers_time = 20
    cooking_time = 90
    total_time = commute_time + grocery_time + dry_cleaning_time + groomers_time + cooking_time
    end_time = start_time + total_time
    hours = end_time // 60
    minutes = end_time % 60
    result = f"{hours}:{minutes:02}"
    return result

print(solution())