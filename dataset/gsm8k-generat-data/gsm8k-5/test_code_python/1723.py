def solution():
    emani_money = 150
    howard_money = emani_money - 30

    # Combine their money
    total_money = emani_money + howard_money

    # Divide the total money equally among them
    each_money = total_money / 2
    result = each_money
    return result

print(solution())