def solution():
    # Calculate the total money earned from selling shirts and pants
    total_money = (5 * 1) + (5 * 3)  # each shirt sells for $1, and each pair of pants sells for $3

    # Calculate the amount of money Kekai gives to his parents
    parents_share = total_money / 2

    # Calculate the amount of money Kekai has left
    money_left = total_money - parents_share
    result = money_left
    return result

print(solution())