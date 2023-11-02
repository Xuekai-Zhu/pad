def solution():
    """Kayden's business delivered an equal number of the 400 cartons of milk it had processed to four of its customers in different towns. However, each of the four customers returned 60 cartons damaged during delivery. What's the total number of cartons that were accepted by the customers?"""
    total_cartons = 400
    returned_cartons = 60 * 4
    accepted_cartons = total_cartons - returned_cartons
    result = accepted_cartons
    return result

print(solution())