def solution():
    """Bogan laid out 10 maggots for her pet beetle. The beetle only ate 1 and Bogan had to throw out the rest. Later that day, she tried feeding again and the beetle ate 3. If Bogan served 20 maggots in total, how many did she attempt to feed the beetle the second time?"""
    # Define the number of maggots laid out during the first feeding
    first_feeding = 10

    # Calculate the number of maggots thrown out
    thrown_out = first_feeding - 1

    # Calculate the number of maggots eaten during the second feeding
    second_feeding = 3

    # Calculate the total number of maggots served
    total_maggots = 20

    # Calculate the number of maggots attempted to feed during the second feeding
    attempted_feeding = total_maggots - first_feeding - thrown_out

    # return the result
    result = attempted_feeding
    return result

print(solution())