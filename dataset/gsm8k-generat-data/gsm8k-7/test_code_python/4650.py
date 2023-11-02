def solution():
    saturday_sandwiches = 2
    sunday_sandwiches = 1
    bread_per_sandwich = 2

    # Calculate the total number of sandwiches Sally eats over the weekend
    total_sandwiches = saturday_sandwiches + sunday_sandwiches

    # Calculate the total number of pieces of bread Sally eats over the weekend
    total_bread = total_sandwiches * bread_per_sandwich
    result = total_bread
    return result

print(solution())