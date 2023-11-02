def solution():
    # Define the initial amount of money
    money = 74

    # Subtract the cost of the sweater and T-shirt
    money -= 9 + 11

    # Subtract the original cost of the shoes and add back the refund
    money -= 30
    money += 0.9 * 30

    result = money
    return result

print(solution())