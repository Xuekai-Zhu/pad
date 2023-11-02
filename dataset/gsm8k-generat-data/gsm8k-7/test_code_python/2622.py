def solution():
    num_jelly_beans_n = 17
    num_jelly_beans_s = num_jelly_beans_n + 4

    # Calculate the sum of Napoleon and Sedrich's jelly beans
    sum_ns = num_jelly_beans_n + num_jelly_beans_s

    # Calculate twice the sum of Napoleon and Sedrich's jelly beans
    twice_sum_ns = 2 * sum_ns

    # Calculate the number of jelly beans that Mikey has
    num_jelly_beans_m = twice_sum_ns / 4
    result = num_jelly_beans_m
    return result

print(solution())