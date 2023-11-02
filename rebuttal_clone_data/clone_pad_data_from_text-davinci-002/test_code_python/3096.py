def solution():
    temperature = 50
    increase_rate = 1.5
    increase_interval = 2
    time_since_increase = 11 - 3
    number_of_increases = time_since_increase / increase_interval
    total_increase = number_of_increases * increase_rate
    final_temperature = temperature + total_increase
    result = final_temperature
    return result

print(solution())