def solution():
    """There were 8000 jelly beans in a certain barrel, and 10 people lined up to take some. The first six people each took twice as many jelly beans as each of the last four people took. If the last four people each took 400 jelly beans, how many jelly beans remained in the container?"""
    # Define the total number of jelly beans in the barrel
    total_jelly_beans = 8000

    # Define the number of people who took jelly beans
    num_people = 10

    # Define the number of jelly beans taken by the last four people
    last_four_jelly_beans = 400

    # Calculate the total number of jelly beans taken by the first six people
    first_six_jelly_beans = 2 * last_four_jelly_beans * 4

    # Calculate the total number of jelly beans taken by everyone
    total_jelly_beans_taken = first_six_jelly_beans + last_four_jelly_beans * 4

    # Calculate the number of jelly beans remaining in the container
    jelly_beans_remaining = total_jelly_beans - total_jelly_beans_taken

    # Display the number of jelly beans remaining
    result = jelly_beans_remaining
    return result

print(solution())