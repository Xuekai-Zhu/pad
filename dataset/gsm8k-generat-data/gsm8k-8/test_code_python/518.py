def solution():
    # Define Selma's number of marbles
    selma_marbles = 50

    # Calculate the total number of marbles Elliot and Merill have
    elliot_marbles = (selma_marbles + 5) / 3
    total_marbles = selma_marbles - 5

    # Calculate Merill's number of marbles
    merill_marbles = 2 * elliot_marbles

    result = merill_marbles
    return result

print(solution())