def solution():
    """Napoleon has 17 jelly beans and Sedrich has 4 more jelly beans than Napoleon. If twice the sum of Napoleon and Sedrich's jelly beans is 4 times the number of jelly beans that Mikey has, how many jelly beans does Mikey have?"""
    # Define the initial number of jelly beans
    napoleon_jelly_beans = 17

    # Define the number of jelly beans Sedrich has
    sedrich_jelly_beans = napoleon_jelly_beans + 4

    # Calculate the sum of jelly beans Napoleon and Sedrich have
    total_jelly_beans = napoleon_jelly_beans + sedrich_jelly_beans

    # Calculate the number of jelly beans Mikey has
    mikey_jelly_beans = total_jelly_beans * 2 / 4

    # Return the result
    result = mikey_jelly_beans
    return result

print(solution())