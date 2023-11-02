def solution():
    permit_cost = 250
    contractor_cost_per_hour = 150
    contractor_hours_per_day = 5
    contractor_num_days = 3
    inspector_discount = 0.8

    # Calculate the total cost of the contractor
    contractor_total_hours = contractor_hours_per_day * contractor_num_days
    contractor_total_cost = contractor_total_hours * contractor_cost_per_hour

    # Calculate the total cost of the inspector
    inspector_cost = contractor_total_cost * (1 - inspector_discount)

    # Calculate the total cost
    total_cost = permit_cost + contractor_total_cost + inspector_cost
    result = total_cost
    return result

print(solution())