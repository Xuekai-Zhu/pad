def solution():
    # Define the initial amount of kibble in the bowl
    initial_kibble = 3

    # Define the final amount of kibble in the bowl
    final_kibble = 1

    # Define the kibble consumption rate
    consumption_rate = 0.25  # 1 pound every 4 hours

    # Calculate the total kibble consumed while Kira was away
    kibble_consumed = initial_kibble - final_kibble

    # Calculate the time Kira was away from home
    time_away = kibble_consumed / consumption_rate
    result = time_away
    return result

print(solution())