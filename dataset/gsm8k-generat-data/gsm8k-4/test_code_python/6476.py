def solution():
    """Today Geoff bought 2 pairs of sneakers and spent $60 equally between the two. Tomorrow, he's going to spend 4 times as much on sneakers than he did on Monday. Wednesday, he'll spend 5 times as much on sneakers than he did on Monday. How much will Geoff spend on sneakers over these three days?"""
    # Define the initial cost of the two pairs of sneakers
    monday_cost = 60/2

    # Define the cost of sneakers on Tuesday and Wednesday
    tuesday_cost = monday_cost * 4
    wednesday_cost = monday_cost * 5

    # Calculate the total cost over three days
    total_cost = monday_cost + tuesday_cost + wednesday_cost

    # return the result
    result = total_cost
    return result

print(solution())