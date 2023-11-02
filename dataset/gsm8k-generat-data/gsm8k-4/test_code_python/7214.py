def solution():
    """Phil started his day with $40. He bought a slice of pizza for $2.75, a soda for $1.50 and a pair of jeans for $11.50. If he has nothing but quarters left of his original money, how many quarters does he now have?"""
    # Define the initial amount of money and the cost of items purchased
    starting_money = 40
    pizza_cost = 2.75
    soda_cost = 1.5
    jeans_cost = 11.5

    # Subtract the cost of items from the initial amount of money
    remaining_money = starting_money - pizza_cost - soda_cost - jeans_cost

    # Convert remaining money into quarters
    quarters = remaining_money / 0.25

    # Round down to the nearest integer
    quarters = int(quarters)

    # return the result
    result = quarters
    return result

print(solution())