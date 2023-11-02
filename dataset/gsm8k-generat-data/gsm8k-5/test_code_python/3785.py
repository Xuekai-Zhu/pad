def solution():
    desired_average = 90  # Kat wants to get a 90% average in her math class
    first_test_score = 95  # Kat got a 95% on her first math test
    second_test_score = 80  # Kat got an 80% on her second math test
    third_test_weight = 3  # The third math test is worth 3 times as much as each of the other tests

    # Calculate the total weight of the first two tests
    first_two_weight = 2

    # Calculate the total weight of all three tests
    total_weight = first_two_weight + third_test_weight

    # Calculate the total score required on the third test to achieve a 90% average
    required_third_test_score = (desired_average* total_weight - first_test_score * first_two_weight - second_test_score * first_two_weight) / third_test_weight
    result = required_third_test_score
    return result

print(solution())