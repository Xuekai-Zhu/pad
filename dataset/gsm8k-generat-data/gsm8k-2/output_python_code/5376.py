def solution():
    """Brianne saves $10 in January. Each month, she saves twice as much as her previous month's savings. How much will she save in May?"""
    savings_jan = 10
    savings_feb = 2 * savings_jan
    savings_mar = 2 * savings_feb
    savings_apr = 2 * savings_mar
    savings_may = 2 * savings_apr
    result = savings_may
    return result

print(solution())