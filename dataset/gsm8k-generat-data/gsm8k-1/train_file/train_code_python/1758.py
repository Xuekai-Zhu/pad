def solution():
    """Jason drives past 3 convenience stores on his way to work. The distance between the first store and the second store is 6 miles. The distance between the second store and third store is 2/3rds longer than the distance between the first two stores. The distance from his house to the first store and the last store to work is the same, 4 miles. How long in miles is Jason's commute to work?"""
    first_to_second = 6
    second_to_third = 6 + (6 * (2/3))
    house_to_first = 4
    last_to_work = 4
    total_distance = first_to_second + second_to_third + house_to_first + last_to_work
    result = total_distance
    return result

print(solution())