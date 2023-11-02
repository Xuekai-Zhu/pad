def solution():
    total_murals = 50  # Two artists painted 50 murals in total

    # Let x be the amount of money Diego got
    # Then, Celina got 4x + $1000
    # And the total paid is x + (4x + $1000) = 5x + $1000
    # So, 5x + $1000 = $50,000
    # Therefore, x = ($50,000 - $1000) / 5
    diego_payment = (50000 - 1000) / 5
    result = diego_payment
    return result

print(solution())