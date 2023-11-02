def solution():
    """Simon is picking blueberries to make blueberry pies. He picks 100 blueberries from his own bushes and another 200 blueberries from blueberry bushes growing nearby. If each pie needs 100 blueberries, how many blueberry pies can Simon make?"""
    # Define the total number of blueberries picked
    total_blueberries = 300

    # Calculate the number of blueberry pies Simon can make
    num_pies = total_blueberries // 100

    # Return the result
    result = num_pies
    return result

print(solution())