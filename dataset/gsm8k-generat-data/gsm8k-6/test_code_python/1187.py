def solution():
    # Calculate the amount of money Brian has left after paying for subway fare and other fruits
    money_left = 50 - (2 * 3.5) - 10 - (0.5 * 10)  # he spends $10 on kiwis and half that much on bananas

    # Find the cost of one apple
    cost_per_apple = 14 / 12  # a bag of dozen apples costs $14

    # Find the maximum number of apples Brian can buy with the money he has left
    max_apples = money_left // cost_per_apple

    result = int(max_apples)
    return result

print(solution())