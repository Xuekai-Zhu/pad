def solution():
    # Define the number of apples and bananas in each purchase
    tony_apples = 2 * 12
    tony_bananas = 1
    arnold_apples = 1 * 12
    arnold_bananas = 1

    # Calculate the cost per apple and per banana
    total_cost = 7 + 5
    apple_cost = total_cost / (tony_apples + arnold_apples)
    banana_cost = total_cost / (tony_bananas + arnold_bananas)

    result = banana_cost
    return result

print(solution())