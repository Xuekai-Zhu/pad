def solution():
    # Define the initial number of jars
    initial_jars = 50 * 20

    # Calculate the number of jars in the reduced delivery
    reduced_jars = (50-20) * 20

    # Calculate the number of damaged jars
    damaged_jars = (3 * 5) + 20

    # Calculate the number of jars available for sale
    good_jars = reduced_jars - damaged_jars

    result = good_jars
    return result

print(solution())