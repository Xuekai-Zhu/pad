def solution():
    """A tomato plant has 100 tomatoes. Jane picks 1/4 of that number for use in their house.
    After a week, she goes back and picks 20 more tomatoes, and the following week picks twice that number.
    What's the total number of fruits remaining on the tomato plant?"""
    
    total_tomatoes = 100
    picked_tomatoes = total_tomatoes / 4
    remaining_tomatoes = total_tomatoes - picked_tomatoes - 20 - (picked_tomatoes * 2)
    result = remaining_tomatoes
    return result

print(solution())