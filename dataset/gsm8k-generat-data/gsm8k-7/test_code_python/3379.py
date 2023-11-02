def solution():
    num_correct_nicole = 22

    # Calculate the number of correct answers for Kim, who answered 3 more than Nicole
    num_correct_kim = num_correct_nicole + 3

    # Calculate the number of correct answers for Cherry, who answered 8 less than Kim
    num_correct_cherry = num_correct_kim - 8

    result = num_correct_cherry
    return result

print(solution())