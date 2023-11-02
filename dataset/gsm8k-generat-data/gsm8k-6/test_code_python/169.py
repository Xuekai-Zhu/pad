def solution():
    # Calculate the amount of grapes used in 6 months
    grapes_in_6_months = 90 

    # Calculate the increased production rate
    increase_rate = 20/100 

    # Calculate the amount of grapes used in a year after increasing production
    grapes_in_a_year = grapes_in_6_months * 2 * (1 + increase_rate) 
    result = grapes_in_a_year
    return result

print(solution())