def solution():
    total_saved = 25 * 6
    bills_paid = total_saved / 3
    coat_cost = 170
    money_needed = coat_cost - (total_saved - bills_paid)
    result = money_needed
    return result

print(solution())