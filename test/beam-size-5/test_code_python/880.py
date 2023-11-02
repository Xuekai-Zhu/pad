def solution():
    
    starting_toys = 200
    toys_given_to_alyssa = 40
    toys_given_to_bonnie = 80
    toys_given_to_nicky = 30
    total_toys_given = toys_given_to_alyssa + toys_given_to_bonnie + toys_given_to_nicky
    remaining_toys = starting_toys - total_toys_given
    result = remaining_toys
    return result

print(solution())