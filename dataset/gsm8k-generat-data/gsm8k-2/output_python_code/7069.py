def solution():
    """Two pieces of bread are needed for one regular sandwich. 3 pieces of bread are needed for a double meat sandwich. How many pieces of bread are needed for 14 regular sandwiches and 12 double meat sandwiches?"""
    regular_sandwiches = 14
    double_sandwiches = 12
    regular_bread = regular_sandwiches * 2
    double_bread = double_sandwiches * 3
    total_bread = regular_bread + double_bread
    result = total_bread
    return result

print(solution())