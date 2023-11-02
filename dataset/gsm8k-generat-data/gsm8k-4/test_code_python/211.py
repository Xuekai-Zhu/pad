def solution():
    """Last year Jessica paid $1000 for rent, $200 for food, and $100 for car insurance each month. This year her rent goes up by 30%, food costs increase by 50%, and the cost of her car insurance triples because she was at fault in an accident. How much more does Jessica pay for her expenses over the whole year compared to last year?"""
    # Define the expenses from last year
    rent_last_year = 1000 * 12
    food_last_year = 200 * 12
    insurance_last_year = 100 * 12

    # Define the expenses from this year
    rent_this_year = 1000 * 1.3 * 12
    food_this_year = 200 * 1.5 * 12
    insurance_this_year = 100 * 3 * 12

    # Calculate the difference in expenses between this year and last year
    difference = (rent_this_year + food_this_year + insurance_this_year) - (rent_last_year + food_last_year + insurance_last_year)

    # Return the result
    result = difference
    return result

print(solution())