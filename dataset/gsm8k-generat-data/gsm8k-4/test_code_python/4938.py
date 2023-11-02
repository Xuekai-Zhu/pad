def solution():
    """Kayden's business delivered an equal number of the 400 cartons of milk it had processed to four of its customers in different towns. However, each of the four customers returned 60 cartons damaged during delivery. What's the total number of cartons that were accepted by the customers?"""
    # Define the number of cartons delivered to each customer
    cartons_delivered = 400 / 4

    # Calculate the number of undamaged cartons accepted by each customer
    cartons_accepted = cartons_delivered - 60

    # Calculate the total number of undamaged cartons accepted by all customers
    total_accepted = cartons_accepted * 4

    result = total_accepted
    return result

print(solution())