def solution():
    """Kayden's business delivered an equal number of the 400 cartons of milk it had processed to four of its customers in different towns. However, each of the four customers returned 60 cartons damaged during delivery. What's the total number of cartons that were accepted by the customers?"""
    total_cartons = 400
    damaged_cartons = 60
    cartons_per_customer = (total_cartons - damaged_cartons) / 4
    total_accepted = cartons_per_customer * 4
    result = total_accepted
    return result

print(solution())