def solution():
    """Jack and Jill shared the cost of renting a cottage that costs $5 an hour. If they rented it for eight hours, how much did each friend pay?"""
    # Define the hourly cost of the cottage
    hourly_cost = 5

    # Define the number of hours the cottage was rented for
    hours_rented = 8

    # Calculate the total cost of renting the cottage
    total_cost = hourly_cost * hours_rented

    # Divide the total cost by the number of friends to get the cost per friend
    cost_per_friend = total_cost / 2

    # Display the cost per friend
    result = cost_per_friend
    return result

print(solution())