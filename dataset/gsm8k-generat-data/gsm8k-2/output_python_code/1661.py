def solution():
    """A tomato plant has 100 tomatoes. Jane picks 1/4 of that number for use in their house. After a week, she goes back and picks 20 more tomatoes, and the following week picks twice that number. What's the total number of fruits remaining on the tomato plant?"""
    initial_tomatoes = 100
    used_tomatoes = initial_tomatoes * 1/4
    remaining_tomatoes = initial_tomatoes - used_tomatoes
    remaining_tomatoes += 20
    remaining_tomatoes += 2 * (remaining_tomatoes / 4)
    result = remaining_tomatoes
    return result

print(solution())