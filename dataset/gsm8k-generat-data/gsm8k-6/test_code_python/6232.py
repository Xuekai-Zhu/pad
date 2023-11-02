def solution():
    # Find the number of girls at the party
    num_girls = 40/4
    # Find the amount of money paid by each girl
    price_girl = 50/2
    # Find the total amount of money paid by girls
    total_girl = num_girls * price_girl
    # Find the total amount of money paid by boys
    total_boys = 40 * 50
    # Calculate the total amount of money collected at the party
    total_money = total_girl + total_boys
    result = total_money
    return result

print(solution())