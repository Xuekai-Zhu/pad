def solution():
    num_turkeys = 2
    turkey_weight = 16  # in pounds
    roast_time = 15  # in minutes per pound
    dinner_time = "6:00 pm"

    # Calculate the total cooking time for each turkey
    total_cooking_time = turkey_weight * roast_time

    # Calculate the total cooking time for both turkeys
    total_cooking_time *= num_turkeys

    # Convert the total cooking time to hours and minutes
    hours = total_cooking_time // 60
    minutes = total_cooking_time % 60

    # Calculate the latest time to start roasting the turkeys
    dinner_hour = int(dinner_time.split(":")[0])
    dinner_minute = int(dinner_time.split(":")[1].split()[0])
    latest_start_hour = dinner_hour - hours
    latest_start_minute = dinner_minute - minutes
    if latest_start_minute < 0:
        latest_start_hour -= 1
        latest_start_minute += 60

    # Format the latest start time as a string
    latest_start_time = "{:02d}:{:02d} pm".format(latest_start_hour, latest_start_minute)

    result = latest_start_time
    return result

print(solution())