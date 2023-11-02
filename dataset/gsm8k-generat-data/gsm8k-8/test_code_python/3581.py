def solution():
    # Calculate total cost of producing and patenting one machine
    total_cost = 3600 + 4500

    # Calculate the revenue from selling one machine
    revenue = 180

    # Determine how many machines Darryl needs to sell to break even
    machines_to_break_even = total_cost / (revenue - total_cost)

    result = machines_to_break_even
    return result

print(solution())