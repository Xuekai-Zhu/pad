def solution():
    """There were 8000 jelly beans in a certain barrel, and 10 people lined up to take some. The first six people each took twice as many jelly beans as each of the last four people took. If the last four people each took 400 jelly beans, how many jelly beans remained in the container?"""
    total_jelly_beans = 8000
    last_four_people_jb = 400
    total_last_four_jb = last_four_people_jb * 4
    total_first_six_jb = total_last_four_jb * 2
    total_first_six_people_jb = total_first_six_jb * 6
    total_jelly_beans_taken = total_first_six_people_jb + total_last_four_jb
    total_jelly_beans_remaining = total_jelly_beans - total_jelly_beans_taken
    result = total_jelly_beans_remaining
    return result

print(solution())