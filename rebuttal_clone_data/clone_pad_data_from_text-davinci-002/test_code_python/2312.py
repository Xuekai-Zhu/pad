def solution():
    total_saved = 1200
    mother_contribution = total_saved * (3/5)
    brother_contribution = mother_contribution * 2
    total_contribution = mother_contribution + brother_contribution
    gift_price = total_saved + total_contribution - 400
    result = gift_price
    return result

print(solution())