def solution():
    """Andy harvests all the tomatoes from 18 plants that have 7 tomatoes each. If he dries half the tomatoes and turns a third of the remainder into marinara sauce, how many tomatoes are left?"""
    # Define the initial number of tomatoes
    tomatoes = 18 * 7

    # Calculate the number of tomatoes that are dried
    dried_tomatoes = tomatoes // 2

    # Calculate the number of tomatoes that are turned into marinara sauce
    sauce_tomatoes = (tomatoes - dried_tomatoes) // 3

    # Calculate the number of tomatoes that are left
    remaining_tomatoes = tomatoes - dried_tomatoes - sauce_tomatoes

    result = remaining_tomatoes
    return result

print(solution())