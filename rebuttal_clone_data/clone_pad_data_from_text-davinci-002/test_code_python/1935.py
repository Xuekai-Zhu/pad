def solution():
    amount_saved = 2900
    spent_in_feb = amount_saved * 0.2
    spent_in_march = amount_saved * 0.4
    spent_in_april = 1500
    total_spent = spent_in_feb + spent_in_march + spent_in_april
    result = amount_saved - total_spent
    return result

print(solution())