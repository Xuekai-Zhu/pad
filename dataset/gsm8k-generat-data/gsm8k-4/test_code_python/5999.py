def solution():
    """Luke takes fifty more than five times as many grape jelly beans as vanilla jelly beans. If there are 120 vanilla jelly beans, how many jelly beans are there in total?"""
    # Define the number of vanilla jelly beans
    vanilla_jelly_beans = 120

    # Calculate the number of grape jelly beans
    grape_jelly_beans = 5 * vanilla_jelly_beans + 50

    # Calculate the total number of jelly beans
    total_jelly_beans = vanilla_jelly_beans + grape_jelly_beans

    result = total_jelly_beans
    return result

print(solution())