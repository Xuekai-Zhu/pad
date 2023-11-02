def solution():
    """Napoleon has 17 jelly beans and Sedrich has 4 more jelly beans than Napoleon. If twice the sum of Napoleon and Sedrich's jelly beans is 4 times the number of jelly beans that Mikey has, how many jelly beans does Mikey have?"""
    # Define the number of jelly beans Napoleon has
    napoleon_jelly_beans = 17

    # Calculate the number of jelly beans Sedrich has
    sedrich_jelly_beans = napoleon_jelly_beans + 4

    # Calculate the sum of Napoleon and Sedrich's jelly beans
    sum_jelly_beans = napoleon_jelly_beans + sedrich_jelly_beans

    # Calculate 4 times the number of jelly beans that Mikey has
    mikey_jelly_beans = sum_jelly_beans * 2 / 4

    # Display the number of jelly beans Mikey has
    result = mikey_jelly_beans
    return result

print(solution())