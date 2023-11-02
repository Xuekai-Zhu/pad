def solution():
    # Calculate the number of files Brennan had left after deleting the irrelevant ones from the first round
    files_after_first_round = 0.3 * 800  # 70% were irrelevant, so 30% were relevant
    # Calculate the number of relevant files Brennan had after downloading the second set
    relevant_files_second_download = 0.4 * (1-0.6) * 400  # 60% were irrelevant, so 40% were relevant
    # Calculate the total number of relevant files Brennan was left with
    total_relevant_files = files_after_first_round + relevant_files_second_download
    result = total_relevant_files
    return result

print(solution())