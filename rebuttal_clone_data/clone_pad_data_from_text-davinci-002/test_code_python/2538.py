def solution():
    total_cents = 175
    cents_given_to_peter = 30
    cents_given_to_randi = 2 * cents_given_to_peter
    total_cents_given = cents_given_to_peter + cents_given_to_randi
    remaining_cents = total_cents - total_cents_given
    nickels_given_to_randi = remaining_cents / 5
    nickels_given_to_peter = cents_given_to_peter / 5
    difference = nickels_given_to_randi - nickels_given_to_peter
    result = difference
    return result

print(solution())