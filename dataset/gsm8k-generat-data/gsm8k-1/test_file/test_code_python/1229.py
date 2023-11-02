def solution():
    """Walter bought 60 apples from the store. He ate 2/5 of them and gave his sister 25% of the remaining number. If he then sold the remaining apples to his uncle at $3 each, how much money did he receive?"""
    total_apples = 60
    apples_eaten = 2/5 * total_apples
    remaining_apples = total_apples - apples_eaten
    apples_given_to_sister = 0.25 * remaining_apples
    apples_sold = remaining_apples - apples_given_to_sister
    price_per_apple = 3
    money_received = apples_sold * price_per_apple
    result = money_received
    return result

print(solution())