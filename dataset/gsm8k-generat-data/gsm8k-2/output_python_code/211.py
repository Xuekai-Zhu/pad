def solution():
    """Last year Jessica paid $1000 for rent, $200 for food, and $100 for car insurance each month. This year her rent goes up by 30%, food costs increase by 50%, and the cost of her car insurance triples because she was at fault in an accident. How much more does Jessica pay for her expenses over the whole year compared to last year?"""
    last_year_rent = 1000 * 12
    last_year_food = 200 * 12
    last_year_insurance = 100 * 12
    this_year_rent = 1000 * 1.3 * 12
    this_year_food = 200 * 1.5 * 12
    this_year_insurance = 100 * 3 * 12
    total_last_year = last_year_rent + last_year_food + last_year_insurance
    total_this_year = this_year_rent + this_year_food + this_year_insurance
    difference = total_this_year - total_last_year
    result = difference
    return result

print(solution())