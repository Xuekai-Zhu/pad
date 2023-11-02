def solution():
    """Mary is counting the number of minnows in the pond. 40% of the minnows have red bellies, 30% have green bellies and the rest have white bellies. If 20 minnows have red bellies, how many minnows have white bellies?"""
    # Define the total number of minnows
    total_minnows = 100

    # Calculate the number of minnows with red bellies
    red_minnows = total_minnows * 0.4

    # Calculate the number of minnows with green bellies
    green_minnows = total_minnows * 0.3

    # Calculate the total number of minnows with red or green bellies
    colored_minnows = red_minnows + green_minnows

    # Calculate the number of minnows with white bellies
    white_minnows = total_minnows - colored_minnows

    # Calculate the number of minnows with red bellies given that 20 minnows have red bellies
    red_minnows = 20

    # Calculate the number of minnows with white bellies
    white_minnows = total_minnows - colored_minnows

    result = white_minnows
    return result

print(solution())