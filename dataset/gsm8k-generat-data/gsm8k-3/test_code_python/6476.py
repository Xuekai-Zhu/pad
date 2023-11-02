def solution():
    """Today Geoff bought 2 pairs of sneakers and spent $60 equally between the two. Tomorrow, he's going to spend 4 times as much on sneakers than he did on Monday. Wednesday, he'll spend 5 times as much on sneakers than he did on Monday. How much will Geoff spend on sneakers over these three days?"""
    # Define the initial cost per pair of sneakers
    initial_cost = 60 / 2 # $30

    # Calculate the cost of sneakers on Tuesday and Wednesday
    tuesday_cost = initial_cost * 4
    wednesday_cost = initial_cost * 5

    # Calculate the total cost over the three days
    total_cost = 60 + tuesday_cost + wednesday_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())