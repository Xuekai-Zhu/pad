def solution():
    """Bogan laid out 10 maggots for her pet beetle. The beetle only ate 1 and Bogan had to throw out the rest. Later that day, she tried feeding again and the beetle ate 3. If Bogan served 20 maggots in total, how many did she attempt to feed the beetle the second time?"""
    # Define the number of maggots served the first time
    maggots_1 = 10

    # Define the number of maggots eaten by the beetle the first time
    eaten_1 = 1

    # Calculate the number of maggots thrown out the first time
    thrown_out = maggots_1 - eaten_1

    # Define the total number of maggots served
    total_maggots = 20

    # Calculate the number of maggots served the second time
    maggots_2 = total_maggots - eaten_1 - thrown_out

    # Display the number of maggots served the second time
    result = maggots_2
    return result

print(solution())