def solution():
    tony_cost = 7
    tony_apples = 2 * 12
    tony_bananas = 1

    arnold_cost = 5
    arnold_apples = 1 * 12
    arnold_bananas = 1

    # Calculate the cost of one apple for Tony
    tony_apple_cost = (tony_cost - (tony_bananas * banana_cost)) / tony_apples

    # Calculate the cost of one apple for Arnold
    arnold_apple_cost = (arnold_cost - (arnold_bananas * banana_cost)) / arnold_apples

    # Calculate the average cost of one apple
    avg_apple_cost = (tony_apple_cost + arnold_apple_cost) / 2

    # Calculate the cost of one bunch of bananas
    banana_cost = (tony_cost - (tony_apples * avg_apple_cost)) / tony_bananas
    result = banana_cost
    return result

print(solution())