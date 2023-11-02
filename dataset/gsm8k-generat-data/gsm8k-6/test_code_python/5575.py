def solution():
    # Find Julia's initial amount of money
    Julia_money = 38 / 2

    # Find the total initial amount of money
    total_money = 38 + Julia_money

    # Find the amount of money their aunt gave each of them
    aunt_money = (97 - total_money) / 2
    result = aunt_money
    return result

print(solution())