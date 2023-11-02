def solution():
    """Carmen needs $7 more to have twice the amount of money that Jethro has. Meanwhile, Patricia has $60, which is 3 times as much as Jethro. What is the sum of all their money?"""
    jethro_money = 60 / 3
    carmen_money = 2 * jethro_money - 7
    total_money = jethro_money + carmen_money + 60
    result = total_money
    return result

print(solution())