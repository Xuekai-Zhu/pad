def solution():
    """Darryl is an inventor who just designed a new machine. He had to pay $3600 for the parts to construct the machine, and $4500 for the patent he applied for once he built it. If the machine sells for $180, how many machines does Darryl need to sell to break even after the costs?"""
    cost_per_machine = 3600 + 4500
    price_per_machine = 180
    machines_to_break_even = cost_per_machine / (price_per_machine * 1.0)
    result = machines_to_break_even
    return result

print(solution())