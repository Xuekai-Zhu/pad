def solution():
    total_money = 300  # $3 is equal to 300 cents
    difference = 50  # Bridget has 50 cents more than Sarah

    # Use algebra to solve for Sarah's money
    # Let x be Sarah's money
    # Then Bridget's money is x + difference
    # And the sum of their money is x + (x + difference) = total_money
    # Simplifying gives 2x = total_money - difference
    # Solving for x gives
    sarah_money = (total_money - difference) / 2

    result = sarah_money
    return result

print(solution())