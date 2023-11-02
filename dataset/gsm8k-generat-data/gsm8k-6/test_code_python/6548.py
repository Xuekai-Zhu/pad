def solution():
    # Calculate the total cost of entry tickets and bus fare for Noah and Ava
    total_cost = (5 * 2) + (1.5 * 2 * 2)  # 5 dollars per person for entry and 1.5 dollars per person for bus fare one way, multiplied by 2 for Noah and Ava

    # Calculate the amount of money left for lunch and snacks
    money_left = 40 - total_cost
    result = money_left
    return result

print(solution())