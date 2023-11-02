def solution():
    total_commute = 21 * 2 # round trip
    gas_cost = 2.5
    car_mpg = 30
    num_people = 5
    num_days_week = 5
    num_weeks = 4

    # Calculate the total amount of gas used for the commute in one month
    total_gas_used = total_commute * num_people * num_days_week * num_weeks / car_mpg

    # Calculate the total gas cost and divide by the number of passengers
    total_gas_cost = total_gas_used * gas_cost
    amount_per_person = total_gas_cost / num_people
    result = amount_per_person
    return result

print(solution())