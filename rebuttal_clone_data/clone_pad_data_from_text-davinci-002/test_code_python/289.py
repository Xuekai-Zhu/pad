def solution():
    """Jim collects model cars, and he has 301 models total. Jim has 4 times as many Buicks as Fords, and 3 more than twice the number of Fords than Chevys. How many Buicks does Jim have?"""
    total_cars = 301
    buicks = 4 * fords
    chevys = 2 * fords + 3
    fords = total_cars - chevys - buicks
    result = buicks
    
    return result

print(solution())