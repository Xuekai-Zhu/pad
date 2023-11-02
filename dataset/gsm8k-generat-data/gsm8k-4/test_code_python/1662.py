def solution():
    """A tomato plant has 100 tomatoes. Jane picks 1/4 of that number for use in their house. After a week, she goes back and picks 20 more tomatoes, and the following week picks twice that number. What's the total number of fruits remaining on the tomato plant?"""
    # Define the initial number of tomatoes
    initial_tomatoes = 100

    # Calculate the number of tomatoes picked by Jane
    jane_tomatoes = initial_tomatoes / 4

    # Calculate the number of tomatoes remaining after Jane's first pick
    remaining_tomatoes = initial_tomatoes - jane_tomatoes

    # Calculate the number of tomatoes picked by Jane on her second pick
    jane_second_pick = 20

    # Calculate the number of tomatoes remaining after Jane's second pick
    remaining_tomatoes -= jane_second_pick

    # Calculate the number of tomatoes picked by Jane on her third pick
    jane_third_pick = jane_second_pick * 2

    # Calculate the number of tomatoes remaining after Jane's third pick
    remaining_tomatoes -= jane_third_pick

    # Return the result
    result = remaining_tomatoes
    return result

print(solution())