def solution():
    # Calculate the total weight of the turkeys
    total_weight = 2 * 16

    # Calculate the total time needed to roast the turkeys
    total_time = total_weight * 15

    # Convert the total time to hours and minutes
    hours = total_time // 60
    minutes = total_time % 60

    # Calculate the latest time Liz can start roasting the turkeys
    latest_time = "4:{} pm".format(60 - minutes) if minutes > 0 else "5:00 pm"

    result = latest_time
    return result

print(solution())