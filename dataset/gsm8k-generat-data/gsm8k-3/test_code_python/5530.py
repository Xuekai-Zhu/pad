def solution():
    """Simon is picking blueberries to make blueberry pies. He picks 100 blueberries from his own bushes and another 200 blueberries from blueberry bushes growing nearby. If each pie needs 100 blueberries, how many blueberry pies can Simon make?"""
    # Define the total number of blueberries picked
    total_blueberries = 100 + 200

    # Calculate the number of pies Simon can make
    pies = total_blueberries // 100

    # Display the number of pies Simon can make
    result = pies
    return result

print(solution())