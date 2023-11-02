def solution():
    initial_pollywogs = 2400
    matured_per_day = 50
    removed_per_day = 10
    removed_days = 20

    # Calculate the total number of pollywogs that will mature and leave the pond
    matured_total = matured_per_day * (removed_days + x)

    # Calculate the remaining number of pollywogs in the pond after Melvin starts removing them
    remaining_pollywogs = initial_pollywogs - (removed_per_day * removed_days)

    # Calculate the number of days it will take for all pollywogs to mature and leave the pond
    days = (remaining_pollywogs / matured_per_day) + removed_days
    result = days
    return result

print(solution())