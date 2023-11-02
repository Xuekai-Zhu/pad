def solution():
    emp1_rate = 20
    emp2_rate = 22
    gov_subsidy = 6  # for hiring disabled worker
    num_hours = 40  # per week

    # Calculate the total weekly cost of employee 1
    emp1_cost = emp1_rate * num_hours

    # Calculate the total weekly cost of employee 2 (with government subsidy)
    emp2_cost = (emp2_rate - gov_subsidy) * num_hours

    # Calculate the weekly savings of hiring employee 1 over employee 2
    savings = emp2_cost - emp1_cost
    result = savings
    return result

print(solution())