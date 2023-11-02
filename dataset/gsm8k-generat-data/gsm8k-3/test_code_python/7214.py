def solution():
    """Phil started his day with $40. He bought a slice of pizza for $2.75, a soda for $1.50 and a pair of jeans for $11.50.
    If he has nothing but quarters left of his original money, how many quarters does he now have?"""
    # Define the starting amount of money and the cost of each item
    starting_money = 40
    pizza_cost = 2.75
    soda_cost = 1.5
    jeans_cost = 11.5

    # Calculate the total cost of the items Phil bought
    total_cost = pizza_cost + soda_cost + jeans_cost

    # Calculate how much money Phil has left
    remaining_money = starting_money - total_cost

    # Calculate how many quarters Phil has
    quarters = int(remaining_money / 0.25)

    # Display the number of quarters Phil has
    result = quarters
    return result

print(solution())