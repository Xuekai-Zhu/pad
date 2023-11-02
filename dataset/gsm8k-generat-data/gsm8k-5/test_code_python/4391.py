def solution():
    quarters = 160  # Libby has 160 quarters in her piggy bank
    cost = 35  # The cost of the dress is $35

    # Convert the cost to quarters
    cost_in_quarters = cost * 4

    # Calculate the number of quarters left after paying for the dress
    quarters_left = quarters - cost_in_quarters
    result = quarters_left
    return result

print(solution())