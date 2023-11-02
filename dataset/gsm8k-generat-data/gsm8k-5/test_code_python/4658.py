def solution():
    total_money = 343  # Toby received $343 from his father
    each_brother_money = (1/7) * total_money  # Toby divided the money equally between his two brothers
    left_money = total_money - (2 * each_brother_money)  # Toby kept the remaining money

    result = left_money
    return result

print(solution())