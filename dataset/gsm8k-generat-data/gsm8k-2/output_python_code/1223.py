def solution():
    """Jim starts with $80 in his investment portfolio. After 1 year it grows by 15%. 
    He then adds another $28 to his portfolio. After 1 more year the combined portfolio grows by 10%. 
    What is his final portfolio worth after 2 years from when he started?"""
    initial_amount = 80
    growth_rate_1 = 0.15
    growth_rate_2 = 0.10
    amount_after_year_1 = initial_amount * (1 + growth_rate_1)
    amount_after_year_2 = (amount_after_year_1 + 28) * (1 + growth_rate_2)
    result = amount_after_year_2
    return result

print(solution())