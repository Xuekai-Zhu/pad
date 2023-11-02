def solution():
    # Calculate the cost of the soda
    initial_amount = 2  # Peter brings $2 with him
    final_amount = 2.5  # Peter leaves with $0.50
    cost_of_soda = initial_amount - final_amount  # Peter spent $1.50 on the soda

    # Calculate the number of ounces of soda Peter bought
    price_per_ounce = 0.25  # The soda costs $0.25 an ounce
    ounces_of_soda = cost_of_soda / price_per_ounce
    result = ounces_of_soda
    return result

print(solution())