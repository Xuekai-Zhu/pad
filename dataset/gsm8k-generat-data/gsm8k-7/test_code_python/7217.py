def solution():
    num_murals = 50
    total_payment = 50000

    # Let x be the amount Diego gets
    # Then Celina gets 4x + 1000

    # Set up the system of equations
    # x + (4x + 1000) = total_payment
    # 5x + 1000 = total_payment
    # 5x = total_payment - 1000
    # x = (total_payment - 1000) / 5

    # Calculate the amount Diego gets
    diego_payment = (total_payment - 1000) / 5
    result = diego_payment
    return result

print(solution())