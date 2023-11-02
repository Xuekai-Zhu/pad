def solution():
    """Andy harvests all the tomatoes from 18 plants that have 7 tomatoes each. If he dries half the tomatoes and turns a third of the remainder into marinara sauce, how many tomatoes are left?"""
    total_tomatoes = 18 * 7
    dried_tomatoes = total_tomatoes / 2
    remaining_tomatoes = total_tomatoes - dried_tomatoes
    marinara_tomatoes = remaining_tomatoes / 3
    remaining_tomatoes = remaining_tomatoes - marinara_tomatoes
    result = remaining_tomatoes
    return result

print(solution())