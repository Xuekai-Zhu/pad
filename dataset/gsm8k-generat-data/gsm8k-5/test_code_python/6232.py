def solution():
    # Calculate the number of girls at the party
    num_girls = len(boys) / 4  # There are 4 times as many boys as girls

    # Calculate the total amount of money collected from boys
    total_boys_money = 40 * 50  # There are 40 boys and each boy paid $50

    # Calculate the amount each girl paid
    girl_payment = total_boys_money / (2 * num_girls)  # Each boy paid twice as much as each girl

    # Calculate the total amount of money collected
    total_money = (num_girls * girl_payment) + total_boys_money
    result = total_money
    return result

print(solution())