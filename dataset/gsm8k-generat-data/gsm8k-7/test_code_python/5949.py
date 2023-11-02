def solution():
    num_cartons = 50
    jars_per_carton = 20

    # Calculate the total number of jars of milk delivered
    total_jars_delivered = num_cartons * jars_per_carton

    # Calculate the number of jars lost due to damaged cartons and jars
    jars_lost = 3 * 5 + jars_per_carton

    # Calculate the number of jars of milk that are good for sale
    jars_for_sale = total_jars_delivered - jars_lost
    result = jars_for_sale
    return result

print(solution())