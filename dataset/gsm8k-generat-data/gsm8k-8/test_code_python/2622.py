def solution():
    # Define the number of jelly beans Napoleon has
    napoleon_jelly_beans = 17

    # Calculate the number of jelly beans Sedrich has
    sedrich_jelly_beans = napoleon_jelly_beans + 4

    # Calculate the sum of jelly beans Napoleon and Sedrich have
    napoleon_sedrich_sum = napoleon_jelly_beans + sedrich_jelly_beans

    # Calculate twice the sum of Napoleon and Sedrich's jelly beans
    double_napoleon_sedrich_sum = 2 * napoleon_sedrich_sum

    # Calculate the number of jelly beans Mikey has
    mikey_jelly_beans = double_napoleon_sedrich_sum / 4

    result = mikey_jelly_beans
    return result

print(solution())