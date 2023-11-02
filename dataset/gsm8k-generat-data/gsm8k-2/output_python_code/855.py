def solution():
    """Randy has some money in his piggy bank. He spends 2 dollars every time he goes to the store. He makes 4 trips to the store every month. If he had $104 dollars left in his piggy bank after a year, how much money, in dollars, did he have at first?"""
    spent_per_month = 2 * 4 # $8 spent per month
    spent_per_year = spent_per_month * 12 # $96 spent per year
    remaining_money = 104 # $104 left after a year
    initial_money = spent_per_year + remaining_money
    result = initial_money
    return result

print(solution())