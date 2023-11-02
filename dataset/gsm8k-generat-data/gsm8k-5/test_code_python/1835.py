def solution():
    # Calculate the total value saved by Teagan in cents
    teagan_savings = 200  # 200 pennies
    teagan_value = teagan_savings / 100  # Convert pennies to dollars

    # Calculate the total value saved by Rex in cents
    rex_savings = 100 * 5  # 100 nickels, each worth 5 cents
    rex_value = rex_savings / 100  # Convert cents to dollars

    # Calculate the total value saved by Toni in cents
    toni_savings = 330 * 10  # 330 dimes, each worth 10 cents
    toni_value = toni_savings / 100  # Convert cents to dollars

    # Calculate the total value saved by all three kids
    total_savings = teagan_savings + rex_savings + toni_savings
    total_value = total_savings / 100  # Convert cents to dollars

    # Return the total value saved by all three kids
    result = total_value
    return result

print(solution())