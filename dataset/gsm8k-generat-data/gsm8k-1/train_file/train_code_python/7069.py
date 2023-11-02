def solution():
    """Two pieces of bread are needed for one regular sandwich. 3 pieces of bread are needed for a double meat sandwich. How many pieces of bread are needed for 14 regular sandwiches and 12 double meat sandwiches?"""
    regular_sandwiches = 14
    double_meat_sandwiches = 12
    bread_per_regular_sandwich = 2
    bread_per_double_meat_sandwich = 3
    total_bread = (regular_sandwiches * bread_per_regular_sandwich) + (double_meat_sandwiches * bread_per_double_meat_sandwich)
    result = total_bread
    return result

print(solution())