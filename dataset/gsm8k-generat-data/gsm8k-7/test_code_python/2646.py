def solution():
    cost_per_semester = 20000
    num_semesters = 2
    num_years = 13

    # Calculate the total cost for one year of school
    yearly_cost = cost_per_semester * num_semesters

    # Multiply the yearly cost by the number of years
    total_cost = yearly_cost * num_years
    result = total_cost
    return result

print(solution())