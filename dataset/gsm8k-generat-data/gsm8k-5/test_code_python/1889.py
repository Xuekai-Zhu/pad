def solution():
    trevor_spending = 80  # Trevor spends $80 every year
    reed_spending = trevor_spending - 20  # Reed spends $20 less than Trevor
    quinn_spending = reed_spending / 2  # Quinn spends half of what Reed spends
    total_spending_per_year = trevor_spending + reed_spending + quinn_spending  # Total spending per year by all three
    total_spending_4_years = total_spending_per_year * 4  # Total spending in 4 years
    result = total_spending_4_years
    return result

print(solution())