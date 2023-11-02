def solution():
    """There were 8000 jelly beans in a certain barrel, and 10 people lined up to take some. The first six people each took twice as many jelly beans as each of the last four people took. If the last four people each took 400 jelly beans, how many jelly beans remained in the container?"""
    # Define the initial number of jelly beans
    jelly_beans = 8000

    # Calculate the total number of jelly beans taken by the last four people
    last_four = 4 * 400

    # Calculate the total number of jelly beans taken by the first six people
    first_six = 2 * 400

    # Calculate the total number of jelly beans taken by all 10 people
    total_taken = (first_six * 6) + (400 * 4)

    # Calculate the number of jelly beans remaining in the barrel
    remaining_jelly_beans = jelly_beans - total_taken

    # Return the result
    result = remaining_jelly_beans
    return result

print(solution())