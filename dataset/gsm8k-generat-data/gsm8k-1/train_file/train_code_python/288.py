def solution():
    """Jim collects model cars, and he has 301 models total. Jim has 4 times as many Buicks as Fords, and 3 more than twice the number of Fords than Chevys. How many Buicks does Jim have?"""
    total_models = 301
    chevy_models = (total_models - 3) / 7
    ford_models = 2 * chevy_models + 3
    buick_models = 4 * ford_models
    result = buick_models
    return result

print(solution())