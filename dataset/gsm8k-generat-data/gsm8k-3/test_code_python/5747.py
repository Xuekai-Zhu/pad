def solution():
    """A bag of jellybeans contains 8 black beans and 2 more green beans. It also contains 1 less orange bean than green beans. How many jellybeans are there in the bag?"""
    # Define the number of black beans and green beans
    black_beans = 8
    green_beans = black_beans + 2

    # Calculate the number of orange beans
    orange_beans = green_beans - 1

    # Calculate the total number of jellybeans
    total_beans = black_beans + green_beans + orange_beans

    # Display the total number of jellybeans
    result = total_beans
    return result

print(solution())