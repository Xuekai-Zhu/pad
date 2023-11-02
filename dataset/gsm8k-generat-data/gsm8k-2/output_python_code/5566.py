def solution():
    """There were 8000 jelly beans in a certain barrel, and 10 people lined up to take some. The first six people each took twice as many jelly beans as each of the last four people took. If the last four people each took 400 jelly beans, how many jelly beans remained in the container?"""
    total_jelly_beans = 8000
    last_four_people_jelly_beans = 400
    last_six_people_jelly_beans = last_four_people_jelly_beans / 2
    total_jelly_beans_taken = 6 * 2 * last_six_people_jelly_beans + 4 * last_four_people_jelly_beans
    remaining_jelly_beans = total_jelly_beans - total_jelly_beans_taken
    result = remaining_jelly_beans
    return result

print(solution())