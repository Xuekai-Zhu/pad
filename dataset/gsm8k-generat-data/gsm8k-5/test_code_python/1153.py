def solution():
    cleaning_cost = 150  # cost of cleaning the pool
    tip_percentage = 0.1  # John gives a 10% tip each time
    chemical_cost = 200  # cost of chemicals per month
    cleaning_frequency = 3  # John gets his pool cleaned every 3 days
    days_in_month = 30  # Average number of days in a month
    
    # Calculate the total cost of pool cleaning per month
    total_cleaning_cost = (cleaning_cost + (cleaning_cost * tip_percentage)) * (days_in_month / cleaning_frequency)
    
    # Calculate the total monthly cost of the pool
    total_cost = total_cleaning_cost + chemical_cost
    result = total_cost
    return result

print(solution())