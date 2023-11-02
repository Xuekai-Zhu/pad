def solution():
    total_jelly_beans = 8000  # There were 8000 jelly beans in the barrel
    last_four_people_jelly_beans = 400  # The last four people each took 400 jelly beans
    last_six_people_jelly_beans = 2 * last_four_people_jelly_beans  # Each of the first six people took twice as many jelly beans as each of the last four people

    # Calculate the total number of jelly beans taken by the last four people
    total_last_four_jelly_beans = last_four_people_jelly_beans * 4

    # Calculate the total number of jelly beans taken by the first six people
    total_first_six_jelly_beans = last_six_people_jelly_beans * 6

    # Calculate the total number of jelly beans taken by all 10 people
    total_taken_jelly_beans = total_last_four_jelly_beans + total_first_six_jelly_beans

    # Calculate the number of jelly beans remaining in the barrel
    remaining_jelly_beans = total_jelly_beans - total_taken_jelly_beans
    result = remaining_jelly_beans
    return result

print(solution())