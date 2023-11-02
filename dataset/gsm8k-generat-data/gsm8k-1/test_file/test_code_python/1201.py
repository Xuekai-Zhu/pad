def solution():
    """Bernie has 4 dogs. They each need a certain amount of exercise per day. The first needs to walk 1 mile. The second needs to walk 4 miles. The third needs to walk 3 miles. On average, they need to walk 3 miles per day. How many miles does the last dog need?"""
    total_miles_needed = 4 * 3
    miles_needed_by_first_three_dogs = 1 + 4 + 3
    miles_needed_by_last_dog = total_miles_needed - miles_needed_by_first_three_dogs
    result = miles_needed_by_last_dog
    return result

print(solution())