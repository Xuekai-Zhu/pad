def solution():
    # Define the cost of a white men's t-shirt
    white_men_cost = 20

    # Calculate the cost of a black men's t-shirt
    black_men_cost = 18

    # Calculate the cost of a white women's t-shirt
    white_women_cost = white_men_cost - 5

    # Calculate the cost of a black women's t-shirt
    black_women_cost = black_men_cost - 5

    # Calculate the total cost of buying t-shirts for men and women in the white sector
    white_sector_cost = 20 * 2 + white_women_cost * 2

    # Calculate the total cost of buying t-shirts for men and women in the black sector
    black_sector_cost = 18 * 2 + black_women_cost * 2

    # Calculate the total cost of buying t-shirts for all employees
    total_cost = white_sector_cost + black_sector_cost

    result = total_cost
    return result

print(solution())