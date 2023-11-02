def solution():
    # Calculate the total cost of the ramp installation
    permit_cost = 250
    contractor_cost = 150 * 3 * 5  # $150 per hour for 3 days of 5 hours each
    inspector_cost = 0.2 * (permit_cost + contractor_cost)  # 80% less than the total cost of permits and contractor
    total_cost = permit_cost + contractor_cost + inspector_cost
    result = total_cost
    return result

print(solution())