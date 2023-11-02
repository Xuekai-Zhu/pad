def solution():
    """Logan's father receives 50 cartons delivery for his milk business, each carton having 20 jars of milk. On a particular week, he received 20 cartons less when the delivery was done, and during offloading, he realized 3 jars in 5 cartons each was damaged, and one carton was totally damaged. How many jars of milk were good for sale that week?"""
    # Define the number of cartons and jars per carton
    initial_cartons = 50
    jars_per_carton = 20

    # Calculate the total number of jars before any damage occurs
    total_jars = initial_cartons * jars_per_carton

    # Calculate the number of cartons received on the particular week
    received_cartons = initial_cartons - 20

    # Calculate the number of cartons with damaged jars
    damaged_cartons = 5
    jars_per_damaged_carton = 20 - 3
    total_damaged_jars = damaged_cartons * jars_per_damaged_carton

    # Calculate the number of jars in the totally damaged carton
    totally_damaged_jars = jars_per_carton

    # Calculate the total number of good jars after the damage has occurred
    total_good_jars = total_jars - total_damaged_jars - totally_damaged_jars

    # return the result
    result = total_good_jars
    return result

print(solution())