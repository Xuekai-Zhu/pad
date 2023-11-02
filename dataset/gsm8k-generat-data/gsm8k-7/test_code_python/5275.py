def solution():
    peggy_stamps = 75

    # Calculate Ernie's stamps
    ernie_stamps = peggy_stamps * 3

    # Calculate Bert's stamps
    bert_stamps = ernie_stamps * 4

    # Calculate the difference between Peggy's and Bert's stamps
    difference = bert_stamps - peggy_stamps

    result = difference
    return result

print(solution())