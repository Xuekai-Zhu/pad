def solution():
    """Janice bought five juices for $10 in total and two sandwiches for $6 in total. How much would she need to pay, if she would only buy one sandwich and one juice?"""
    # Calculate the cost per juice
    juice_cost = 10 / 5

    # Calculate the cost per sandwich
    sandwich_cost = 6 / 2

    # Calculate the total cost of one juice and one sandwich
    total_cost = juice_cost + sandwich_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())