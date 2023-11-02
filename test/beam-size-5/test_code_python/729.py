def solution():
    num_siblings = 3
    found_money = 20

    # Calculate the total amount of money Greg has
    total_money = found_money + (num_siblings * found_money)

    # Divide the total money equally among the siblings
    money_per_sibling = total_money / 2
    result = money_per_sibling
    return result

print(solution())