def solution():
    # Calculate total cost of making the pies
    pumpkin_pie_cost = 10 * 3
    cherry_pie_cost = 12 * 5
    total_cost = pumpkin_pie_cost + cherry_pie_cost

    # Calculate total revenue required to make a profit of $20
    total_revenue = total_cost + 20

    # Calculate the number of pies that Benny is making
    total_pies = 10 + 12

    # Calculate the price per pie required to make the required revenue
    price_per_pie = total_revenue / total_pies
    result = price_per_pie
    return result

print(solution())