def solution():
    jethro_money = 60 / 3  # Patricia has $60, which is 3 times as much as Jethro
    carmen_money = (2 * jethro_money) - 7  # Carmen needs $7 more to have twice the amount of money that Jethro has
    total_money = jethro_money + carmen_money + 60  # Total sum of money

    result = total_money
    return result

print(solution())