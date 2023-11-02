def solution():
    # Calculate the amount of coffee left in the cup after Omar drinks 1/4 and then 1/2
    remaining_coffee = 12 * (1 - 1/4) * (1 - 1/2)
    # Subtract the 1 ounce that Omar drinks later in the day
    final_coffee = remaining_coffee - 1
    result = final_coffee
    return result

print(solution())