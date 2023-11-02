def solution():
    # Calculate the total number of marbles Carl has after his mother brings him a bag of marbles
    original_marbles = 12  # Carl takes out 12 marbles
    remaining_marbles = original_marbles * (1/2)  # Carl loses half of the marbles he took out
    new_marbles = 10  # Carl takes out 10 more marbles
    total_marbles = original_marbles - remaining_marbles + new_marbles + 25  # Carl adds the new bag of marbles to the remaining marbles he has left after the accident and the ones he took out later
    result = total_marbles
    return result

print(solution())