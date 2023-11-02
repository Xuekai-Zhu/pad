def solution():
    # Calculate the total number of coals burned by the grill
    total_coals_burned = 15 * 3 * 60  # 15 coals burnt every 20 minutes, 3 bags of coal, each containing 60 coals

    # Calculate the total grilling time in minutes
    grilling_time = total_coals_burned / 15 * 20  # 15 coals burnt every 20 minutes

    # Convert grilling time to hours and minutes
    hours = int(grilling_time / 60)
    minutes = int(grilling_time % 60)

    result = f"{hours} hours and {minutes} minutes"
    return result

print(solution())