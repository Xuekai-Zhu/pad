def solution():
    """Nadia was sent to the flower shop to buy 20 roses and 3/4 times as many Lillies as roses. If roses cost $5 each and lilies cost twice as much each, calculate the total amount of money Nadia used to buy the flowers."""
    # Define the number of roses to be bought
    roses = 20

    # Calculate the number of lilies to be bought
    lilies = int(3/4 * roses)

    # Define the prices of roses and lilies
    rose_price = 5
    lily_price = 2 * rose_price

    # Calculate the total cost of buying the flowers
    total_cost = (roses * rose_price) + (lilies * lily_price)

    # return the result
    result = total_cost
    return result

print(solution())