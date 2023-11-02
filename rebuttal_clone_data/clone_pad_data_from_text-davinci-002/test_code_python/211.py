def solution():
    """Last year Jessica paid $1000 for rent, $200 for food, and $100 for car insurance each month. This year her rent goes up by 30%, food costs increase by 50%, and the cost of her car insurance triples because she was at fault in an accident. How much more does Jessica pay for her expenses over the whole year compared to last year?"""
    rent_last_year = 1000
    food_last_year = 200
    insurance_last_year = 100
    rent_increase = 30
    food_increase = 50
    insurance_increase = 300
    rent_this_year = rent_last_year + (rent_last_year * (rent_increase / 100))
    food_this_year = food_last_year + (food_last_year * (food_increase / 100))
    insurance_this_year = insurance_last_year + (insurance_last_year * (insurance_increase / 100))
    total_increase = rent_this_year + food_this_year + insurance_this_year
    result = total_increase

print(solution())