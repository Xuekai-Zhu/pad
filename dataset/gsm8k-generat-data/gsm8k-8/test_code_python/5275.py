def solution():
    # Calculate Ernie's number of stamps
    ernie_stamps = 3 * 75

    # Calculate Bert's number of stamps
    bert_stamps = 4 * ernie_stamps

    # Calculate the number of stamps Peggy needs to add
    peggy_stamps_needed = bert_stamps - 75

    result = peggy_stamps_needed
    return result

print(solution())