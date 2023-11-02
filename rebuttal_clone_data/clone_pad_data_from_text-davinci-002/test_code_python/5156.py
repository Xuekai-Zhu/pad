def solution():
    cows_before = 39
    cows_lost = 25
    cows_sold = 6
    cows_gained = 24
    cows_bought = 43
    cows_given = 8
    cows_now = cows_before + cows_gained + cows_bought + cows_given - cows_sold - cows_lost
    result = cows_now
    return result

print(solution())