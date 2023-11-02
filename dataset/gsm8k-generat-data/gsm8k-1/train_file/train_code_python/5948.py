def solution():
    """Logan's father receives 50 cartons delivery for his milk business, each carton having 20 jars of milk. On a particular week, he received 20 cartons less when the delivery was done, and during offloading, he realized 3 jars in 5 cartons each was damaged, and one carton was totally damaged. How many jars of milk were good for sale that week?"""
    cartons_received = 50
    jars_per_carton = 20
    cartons_received -= 20
    damaged_cartons = 5
    jars_damaged_per_carton = 3
    total_jars_damaged = (damaged_cartons * jars_damaged_per_carton) + jars_per_carton
    total_jars = (cartons_received * jars_per_carton) - total_jars_damaged
    result = total_jars
    return result

print(solution())