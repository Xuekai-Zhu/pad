def solution():
    shoes_cost = 80  # Jillian's shoes cost $80
    handbag_cost = 3 * shoes_cost - 20  # Jillian's handbag cost $20 less than 3 times as much as her shoes cost

    # Calculate Jillian's bag cost
    bag_cost = handbag_cost + shoes_cost
    result = bag_cost
    return result

print(solution())