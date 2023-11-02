def solution():
    initial_population = 2400  # Elmer initially had 2400 pollywogs in his pond
    pollywogs_leaving_rate = 50  # Polliwogs matured into toads and left the pond at a constant rate of 50 per day

    # Calculate the number of days it took for all the pollywogs to turn into toads and leave the pond
    days_till_all_pollywogs_left = initial_population // pollywogs_leaving_rate

    # Calculate the number of pollywogs caught and released by Melvin
    pollywogs_caught_by_melvin = 10 * 20  # Melvin caught 10 pollywogs per day for 20 days

    # Calculate the remaining number of pollywogs
    remaining_pollywogs = initial_population - (pollywogs_leaving_rate * days_till_all_pollywogs_left) - pollywogs_caught_by_melvin

    # Calculate the number of days it took for all the remaining pollywogs to disappear from the pond
    days_till_no_pollywogs_left = remaining_pollywogs // pollywogs_leaving_rate

    # Calculate the total number of days it took for all the pollywogs to disappear from the pond
    total_days = days_till_all_pollywogs_left + 20 + days_till_no_pollywogs_left
    result = total_days
    return result

print(solution())