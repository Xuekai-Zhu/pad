def solution():
    max_rum_consumption = 30  # Don can consume a maximum of 3 times the amount of rum given to him
    total_rum_consumed = 10 + 12  # Don already consumed 12oz earlier that day and 10oz on his pancakes

    # Calculate the maximum amount of rum Don can have after eating all of the rum and pancakes
    remaining_rum = max_rum_consumption - total_rum_consumed
    result = remaining_rum
    return result

print(solution())