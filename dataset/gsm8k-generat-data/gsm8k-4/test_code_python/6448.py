def solution():
    """Six kids and two adults are going to the circus. Kid's tickets are on sale for only half of the adult tickets. The total cost is $50. How much is one kid's ticket?"""
    # Define the number of kids and adults, and the total cost
    kids = 6
    adults = 2
    total_cost = 50

    # Define the price of an adult ticket as x
    x = 1

    # Define the price of a kid's ticket as half of the adult ticket
    y = 0.5

    # Calculate the total cost based on the number of tickets sold and their prices
    total = (kids * y * x) + (adults * x)

    # Calculate the price of one kid's ticket by dividing the total cost by the number of kids
    kid_ticket_price = (total_cost - (adults * x)) / (kids * y)

    # return the result
    result = kid_ticket_price
    return result

print(solution())