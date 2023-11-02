def solution():
    """In a building, there are a hundred ladies on the first-floor studying. There are three times that many girls at a party being held on the second floor of the building. How many ladies are on the two floors in total?"""
    ladies_on_first_floor = 100
    girls_on_second_floor = 3 * ladies_on_first_floor
    total_ladies = ladies_on_first_floor + girls_on_second_floor
    result = total_ladies
    return result

print(solution())