def solution():
    # Define the initial number of gumballs for Joanna and Jacques
    joanna_initial = 40
    jacques_initial = 60

    # Calculate the total initial number of gumballs
    total_initial = joanna_initial + jacques_initial

    # Calculate the number of gumballs they purchased and added
    purchased = 4 * total_initial

    # Calculate the total number of gumballs
    total = total_initial + purchased

    # Calculate the number of gumballs each person gets when shared equally
    each_gets = total / 2
    result = each_gets
    return result

print(solution())