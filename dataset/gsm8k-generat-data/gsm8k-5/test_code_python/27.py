def solution():
    # Calculate the number of files Brennan deleted after the first round
    deleted_first_round = int(0.7 * 800)

    # Calculate the number of valuable files Brennan had after the first round
    valuable_first_round = 800 - deleted_first_round

    # Calculate the number of files Brennan deleted after the second round
    deleted_second_round = int(0.6 * 400)

    # Calculate the number of valuable files Brennan had after the second round
    valuable_second_round = 400 - deleted_second_round

    # Calculate the total number of valuable files Brennan was left with
    total_valuable_files = valuable_first_round + valuable_second_round
    result = total_valuable_files
    return result

print(solution())