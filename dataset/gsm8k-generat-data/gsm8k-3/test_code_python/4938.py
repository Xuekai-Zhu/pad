def solution():
    """Kayden's business delivered an equal number of the 400 cartons of milk it had processed to four of its customers in different towns. However, each of the four customers returned 60 cartons damaged during delivery. What's the total number of cartons that were accepted by the customers?"""
    # Calculate the initial number of cartons delivered to each customer
    initial_deliveries = 400 // 4

    # Calculate the number of cartons accepted by each customer
    accepted_cartons = initial_deliveries - 60

    # Calculate the total number of cartons accepted by all customers
    total_accepted = accepted_cartons * 4

    # Display the total number of cartons accepted
    result = total_accepted
    return result

print(solution())