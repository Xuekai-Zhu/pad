def solution():
    """When Matty was born, the cost of a ticket to Mars was $1,000,000. The cost is halved every 10 years. How much will a ticket cost when Matty is 30?"""
    # Define the initial cost of the ticket
    initial_cost = 1000000

    # Calculate the number of times the cost is halved in 30 years
    halvings = 3

    # Calculate the final cost of the ticket
    final_cost = initial_cost / (2 ** halvings)

    # Display the final cost of the ticket
    result = final_cost
    return result

print(solution())