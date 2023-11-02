def solution():
    # Find the total number of jelly beans taken by the last four people
    jelly_beans_last_four = 4 * 400

    # Find the total number of jelly beans taken by the first six people
    jelly_beans_first_six = 2 * 400 * 6

    # Find the total number of jelly beans taken by all the people
    total_jelly_beans_taken = jelly_beans_last_four + jelly_beans_first_six

    # Find the number of jelly beans that remained in the container
    jelly_beans_remaining = 8000 - total_jelly_beans_taken
    result = jelly_beans_remaining
    return result

print(solution())