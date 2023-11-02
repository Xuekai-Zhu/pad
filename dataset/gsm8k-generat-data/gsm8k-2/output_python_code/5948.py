def solution():
    """Logan's father receives 50 cartons delivery for his milk business, each carton having 20 jars of milk. On a particular week, he received 20 cartons less when the delivery was done, and during offloading, he realized 3 jars in 5 cartons each was damaged, and one carton was totally damaged. How many jars of milk were good for sale that week?"""
    cartons_received = 50
    jars_per_carton = 20
    cartons_received -= 20  # adjust for missing delivery
    total_jars = cartons_received * jars_per_carton
    damaged_cartons = 5
    jars_per_damaged_carton = 23
    total_damaged_jars = (damaged_cartons * jars_per_damaged_carton) + jars_per_carton
    good_jars = total_jars - total_damaged_jars
    result = good_jars
    return result

print(solution())