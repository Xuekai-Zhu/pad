def solution():
    peggy_stamps = 75  # Peggy currently has 75 stamps
    ernie_stamps = 3 * peggy_stamps  # Ernie has three times as many stamps as Peggy
    bert_stamps = 4 * ernie_stamps  # Bert has four times as many stamps as Ernie

    # Calculate the difference in the number of stamps Peggy needs to add to her collection
    diff = bert_stamps - peggy_stamps

    result = diff
    return result

print(solution())