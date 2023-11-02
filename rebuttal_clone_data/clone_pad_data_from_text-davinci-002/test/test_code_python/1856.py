def solution():
    owed_by_all = 400
    paid_so_far = 285
    money_still_owed = owed_by_all - paid_so_far
    Amy_owed = 30
    Derek_owed = Amy_owed / 2
    Sally_and_Carl_owed = money_still_owed - (Amy_owed + Derek_owed)
    Sally_and_Carl_each_owed = Sally_and_Carl_owed / 2
    result = Sally_and_Carl_each_owed
    return result

print(solution())