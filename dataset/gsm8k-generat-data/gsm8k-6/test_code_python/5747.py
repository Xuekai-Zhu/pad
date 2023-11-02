def solution():
    # Calculate the number of green beans
    green_beans = 8 + 2  # the bag contains 2 more green beans than black beans

    # Calculate the number of orange beans
    orange_beans = green_beans - 1  # the bag contains 1 less orange bean than green beans

    # Calculate the total number of jellybeans in the bag
    total_jellybeans = 8 + green_beans + orange_beans

    result = total_jellybeans
    return result

print(solution())