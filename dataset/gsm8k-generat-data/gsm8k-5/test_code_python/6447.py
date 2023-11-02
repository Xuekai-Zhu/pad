def solution():
    cost_per_apple = 2  # Each apple costs $2
    emmy_money = 200  # Emmy has $200
    gerry_money = 100  # Gerry has $100

    # Calculate the number of apples Emmy and Gerry can buy individually
    emmy_apples = emmy_money // cost_per_apple
    gerry_apples = gerry_money // cost_per_apple

    # Calculate the total number of apples Emmy and Gerry can buy together
    total_apples = emmy_apples + gerry_apples
    result = total_apples
    return result

print(solution())