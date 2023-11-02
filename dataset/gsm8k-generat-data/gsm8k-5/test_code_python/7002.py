def solution():
    turkeys = 2  # Liz roasts 2 turkeys
    weight_per_turkey = 16  # Each turkey weighs 16 pounds
    time_per_pound = 15  # Each pound of turkey takes 15 minutes to roast
    max_start_time = "N/A"  # Initialize the latest start time to N/A, in case it cannot be calculated

    # Calculate the total roasting time for both turkeys
    total_roasting_time = turkeys * weight_per_turkey * time_per_pound

    # Dinner is served at 6:00 pm, so Liz needs to start roasting the turkeys no later than 6:00 pm minus the total roasting time
    if total_roasting_time <= 540:  # If the total roasting time is less than or equal to 9 hours (540 minutes)
        hours = total_roasting_time // 60
        minutes = total_roasting_time % 60
        max_start_time = f"{6 - hours}:{60 - minutes if minutes > 0 else '00'} pm"  # Calculate the latest start time in the "hh:mm pm" format

    result = max_start_time
    return result

print(solution())