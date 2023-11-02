def solution():
    # Calculate the total amount of money Asha has
    total_money = 20 + 40 + 30 + 70 + 100  # $20 borrowed from brother, $40 from father, $30 from mother, $70 gifted by granny, $100 in savings

    # Calculate the amount of money Asha spent
    spent_money = 3/4 * total_money

    # Calculate the amount of money Asha has left
    remaining_money = total_money - spent_money
    result = remaining_money
    return result

print(solution())