def solution():
    """Last year Jessica paid $1000 for rent, $200 for food, and $100 for car insurance each month. This year her rent goes up by 30%, food costs increase by 50%, and the cost of her car insurance triples because she was at fault in an accident. How much more does Jessica pay for her expenses over the whole year compared to last year?"""
    # Define the expenses from last year
    rent_last_year = 1000 * 12
    food_last_year = 200 * 12
    car_insurance_last_year = 100 * 12

    # Calculate the expenses from this year
    rent_this_year = 1.3 * rent_last_year
    food_this_year = 1.5 * food_last_year
    car_insurance_this_year = 3 * car_insurance_last_year

    # Calculate the difference in expenses
    difference = (rent_this_year + food_this_year + car_insurance_this_year) - (rent_last_year + food_last_year + car_insurance_last_year)

    # Display the difference in expenses
    result = difference
    return result

print(solution())