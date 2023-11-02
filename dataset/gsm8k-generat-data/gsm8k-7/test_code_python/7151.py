def solution():
    yearly_visits = 12
    yearly_cost = 5

    # Calculate the total cost of visiting the museum for the first year
    total_cost = yearly_visits * yearly_cost

    # Calculate the total cost of visiting the museum for the second year
    yearly_visits = 4
    yearly_cost = 7
    total_cost += yearly_visits * yearly_cost

    # Calculate the total cost of visiting the museum for the third year
    total_cost += yearly_visits * yearly_cost

    # Calculate the total cost of visiting the museum for three years
    total_cost *= 3
    result = total_cost
    return result

print(solution())