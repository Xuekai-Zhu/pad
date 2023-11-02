def solution():
    """John gets his pool cleaned every 3 days. It cost $150 each time and he gives the guy a 10% tip each time he comes to clean. Then twice a month he needs to use $200 of chemicals. How much does his pool cost a month?"""

    # Calculate the cost of pool cleaning for one month
    cleanings_per_month = 30/3 # John gets his pool cleaned every 3 days, so there are 30/3=10 cleanings in a month
    cleaning_cost = cleanings_per_month * 150 # Each cleaning costs $150
    tip = cleaning_cost * 0.1 # John gives a 10% tip each time the pool is cleaned
    total_cleaning_cost = cleaning_cost + tip # Total cost of pool cleaning including tip

    # Calculate the cost of chemicals for one month
    chemical_cost = 200 * 2 # John needs to use $200 of chemicals twice a month

    # Calculate the total cost of maintaining the pool for one month
    total_cost = total_cleaning_cost + chemical_cost

    # Display the total cost of maintaining the pool for one month
    result = total_cost
    return result

print(solution())