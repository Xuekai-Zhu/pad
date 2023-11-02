def solution():
    lisa_saved = 1200
    mother_contribution = 3/5 * lisa_saved
    brother_contribution = 2 * mother_contribution
    total_money = lisa_saved + mother_contribution + brother_contribution
    price_of_gift = total_money - 400
    result = price_of_gift
    return result

print(solution())