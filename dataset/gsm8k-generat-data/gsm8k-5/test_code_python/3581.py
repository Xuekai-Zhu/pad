def solution():
    cost_per_machine = 3600 + 4500  # Darryl's total cost per machine
    selling_price = 180  # The price at which Darryl is selling each machine

    # Calculate the number of machines needed to break even
    machines_needed = cost_per_machine / (selling_price - cost_per_machine)

    result = machines_needed
    return result

print(solution())