def solution():
    # Calculate the number of pollywogs that left the pond
    lost_pollywogs = 50 * 20  # 50 pollywogs left the pond per day for 20 days

    # Calculate the number of pollywogs remaining
    remaining_pollywogs = 2400 - lost_pollywogs

    # Calculate the number of days it will take for Melvin to catch all the remaining pollywogs
    days_to_catch = remaining_pollywogs / 10  # Melvin catches 10 pollywogs per day

    # Calculate the total number of days it will take for all the pollywogs to disappear from the pond
    total_days = 20 + days_to_catch

    result = total_days
    return result

print(solution())