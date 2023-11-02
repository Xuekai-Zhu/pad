def solution():
    # Calculate the total cost to produce one machine
    total_cost = 3600 + 4500  # $3600 for parts + $4500 for patent
    price_per_machine = 180  # selling price per machine
    machines_to_break_even = total_cost / price_per_machine  # calculate the number of machines to break even
    result = machines_to_break_even
    return result

print(solution())