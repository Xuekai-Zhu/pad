def solution():
    """It takes 50 large jelly beans to fill up a large drinking glass. It takes half that amount to fill up a small drinking glass. If there are 5 large drinking glasses and 3 small ones, how many jellybeans will it take to fill them up?"""
    # Define the number of large jelly beans required per glass
    large_jelly_beans_per_glass = 50

    # Define the number of small jelly beans required per glass
    small_jelly_beans_per_glass = large_jelly_beans_per_glass // 2

    # Define the number of large glasses and small glasses
    num_large_glasses = 5
    num_small_glasses = 3

    # Calculate the total number of jelly beans required
    total_jelly_beans = (large_jelly_beans_per_glass * num_large_glasses) + (small_jelly_beans_per_glass * num_small_glasses)

    result = total_jelly_beans
    return result

print(solution())