def solution():
    # Calculate Jethro's amount of money
    jethro_money = 60 / 3

    # Calculate twice Jethro's amount of money
    twice_jethro_money = 2 * jethro_money

    # Calculate Carmen's amount of money
    carmen_money = twice_jethro_money - 7

    # Calculate the sum of all their money
    sum_of_money = jethro_money + carmen_money + 60
    result = sum_of_money
    return result

print(solution())