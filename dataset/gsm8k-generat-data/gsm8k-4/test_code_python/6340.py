def solution():
    """Blake wants to spend his Friday making milkshakes for his family. He knows that he needs 4 ounces of milk and 12 ounces of ice cream for each milkshake. If he has 72 ounces of milk and 192 ounces of ice cream, how much milk will be left over when he is done?"""
    # Calculate the maximum number of milkshakes that can be made with the available milk and ice cream
    max_milkshakes_milk = 72 // 4
    max_milkshakes_icecream = 192 // 12
    max_milkshakes = min(max_milkshakes_milk, max_milkshakes_icecream)

    # Calculate the total amount of milk used to make the maximum number of milkshakes
    total_milk_used = max_milkshakes * 4

    # Calculate the amount of milk left over
    milk_left_over = 72 - total_milk_used

    result = milk_left_over
    return result

print(solution())