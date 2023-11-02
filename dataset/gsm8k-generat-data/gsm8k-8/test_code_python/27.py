def solution():
    # Define the number of files Brennan downloaded in the first round
    first_round = 800

    # Calculate how many files were not helpful in the first round
    not_helpful_first_round = 0.7 * first_round

    # Calculate how many files were left after deleting the irrelevant ones in the first round
    helpful_first_round = first_round - not_helpful_first_round

    # Define the number of files Brennan downloaded in the second round
    second_round = 400

    # Calculate how many files were not helpful in the second round
    not_helpful_second_round = 0.6 * second_round

    # Calculate how many files were left after deleting the irrelevant ones in the second round
    helpful_second_round = second_round - not_helpful_second_round

    # Calculate the total number of valuable files Brennan was left with
    total_valuable_files = helpful_first_round + helpful_second_round
    result = total_valuable_files
    return result

print(solution())