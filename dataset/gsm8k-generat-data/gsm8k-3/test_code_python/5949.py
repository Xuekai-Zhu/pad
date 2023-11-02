def solution():
    """Logan's father receives 50 cartons delivery for his milk business, each carton having 20 jars of milk. On a particular week, he received 20 cartons less when the delivery was done, and during offloading, he realized 3 jars in 5 cartons each was damaged, and one carton was totally damaged. How many jars of milk were good for sale that week?"""
    # Define the number of cartons and jars per carton
    CARTONS_DELIVERY = 50
    JARS_PER_CARTON = 20

    # Calculate the number of cartons received that week
    cartons_received = CARTONS_DELIVERY - 20

    # Calculate the number of jars that were damaged
    jars_damaged = (5 * 3) + JARS_PER_CARTON

    # Calculate the number of jars that were good for sale
    jars_for_sale = (cartons_received * JARS_PER_CARTON) - jars_damaged

    # Display the number of jars for sale
    result = jars_for_sale
    return result

print(solution())