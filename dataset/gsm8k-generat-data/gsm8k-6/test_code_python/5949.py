def solution():
    # Calculate the total number of jars of milk received
    total_jars = 50 * 20  # 50 cartons each having 20 jars of milk

    # Calculate the number of jars of milk in the damaged cartons
    damaged_jars = 3 * 5  # 3 jars in 5 cartons each

    # Calculate the total number of jars of milk that are not good for sale
    total_damaged_jars = damaged_jars + 20  # 1 carton was totally damaged

    # Calculate the number of jars of milk that are good for sale
    good_jars = total_jars - total_damaged_jars

    result = good_jars
    return result

print(solution())