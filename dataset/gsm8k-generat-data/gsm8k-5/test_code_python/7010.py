def solution():
    cost_potato_chips = 3 * 1.0  # Alex buys 3 individual bags of potato chips for $1.00 each
    cost_creme_fraiche = 5.0  # The creme fraiche costs $5.00
    cost_caviar = 73.0  # The caviar costs $73.00
    num_people = 3  # The appetizer will serve 3 people

    # Calculate the total cost of the appetizer
    total_cost = cost_potato_chips + cost_creme_fraiche + cost_caviar

    # Calculate the cost per person
    cost_per_person = total_cost / num_people
    result = cost_per_person
    return result

print(solution())