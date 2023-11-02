def solution():
    initial_nickels = 95
    cents_given_to_peter = 25
    cents_given_to_randi = 2 * cents_given_to_peter
    total_cents_given = cents_given_to_peter + cents_given_to_randi
    final_nickels = initial_nickels - total_cents_given
    result = final_nickels
    return result

print(solution())