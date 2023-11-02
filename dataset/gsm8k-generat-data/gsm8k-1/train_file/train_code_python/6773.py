def solution():
    """At a certain car dealership, 15% of the cars cost less than $15000 and 40% of the cars cost more than $20000. If there are 3000 cars at the dealership, how many of them cost between $15000 and $20000?"""
    total_cars = 3000
    less_than_15000 = int(total_cars * 0.15)
    more_than_20000 = int(total_cars * 0.40)
    between_15000_20000 = total_cars - less_than_15000 - more_than_20000
    result = between_15000_20000

    return result

print(solution())