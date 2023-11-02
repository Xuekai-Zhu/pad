def solution():
    # Calculate the total cost of the appetizer
    cost_potato_chips = 3 * 1.0  # 3 individual bags of potato chips for $1.00 each
    cost_creme_fraiche = 5.0  # cost of creme fraiche
    cost_caviar = 73.0  # cost of caviar
    total_cost = cost_potato_chips + cost_creme_fraiche + cost_caviar

    # Calculate the cost per person
    cost_per_person = total_cost / 3
    result = cost_per_person
    return result

print(solution())