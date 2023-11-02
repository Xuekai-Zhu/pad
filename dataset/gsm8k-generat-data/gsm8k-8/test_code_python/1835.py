def solution():
    # Define the values for each child's savings
    teagan_savings = 200
    rex_savings = 100 * 5 # 100 nickels is equal to 500 cents, or $5
    toni_savings = 330 * 10 # 330 dimes is equal to 3300 cents, or $33

    # Add up the savings of all three children
    total_savings = teagan_savings + rex_savings + toni_savings
    result = total_savings
    return result

print(solution())