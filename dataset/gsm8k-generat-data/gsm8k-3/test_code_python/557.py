def solution():
    """Andy harvests all the tomatoes from 18 plants that have 7 tomatoes each. If he dries half the tomatoes and turns a third of the remainder into marinara sauce, how many tomatoes are left?"""
    # Calculate the total number of tomatoes
    total_tomatoes = 18 * 7

    # Calculate the number of tomatoes dried
    dried_tomatoes = total_tomatoes / 2

    # Calculate the number of remaining tomatoes
    remaining_tomatoes = total_tomatoes - dried_tomatoes

    # Calculate the number of tomatoes turned into marinara sauce
    marinara_tomatoes = remaining_tomatoes / 3

    # Calculate the number of tomatoes left
    tomatoes_left = remaining_tomatoes - marinara_tomatoes

    # Display the number of tomatoes left
    result = tomatoes_left
    return result

print(solution())