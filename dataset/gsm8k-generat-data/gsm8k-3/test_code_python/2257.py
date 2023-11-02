def solution():
    """There are 4,000 jelly beans in a jar. If three fourths of the jelly beans are red, and one quarter of the red jelly beans are coconut flavored, how many jelly beans are coconut flavored?"""
    # Define the total number of jelly beans in the jar
    total_jelly_beans = 4000

    # Calculate the number of red jelly beans
    red_jelly_beans = 3 / 4 * total_jelly_beans

    # Calculate the number of coconut-flavored jelly beans
    coconut_jelly_beans = 1 / 4 * red_jelly_beans

    # Display the number of coconut-flavored jelly beans
    result = coconut_jelly_beans
    return result

print(solution())