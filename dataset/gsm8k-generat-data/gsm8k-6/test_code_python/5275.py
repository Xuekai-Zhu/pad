def solution():
    # Find Ernie's and Bert's current number of stamps
    ernie_stamps = 3 * 75  # Peggy has 75 stamps, and Ernie has three times as many stamps as Peggy
    bert_stamps = 4 * ernie_stamps  # Bert has four times as many stamps as Ernie

    # Find the number of stamps Peggy needs to add to have as many stamps as Bert
    stamps_to_add = bert_stamps - 75
    result = stamps_to_add
    return result

print(solution())