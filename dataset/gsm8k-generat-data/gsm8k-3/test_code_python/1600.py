def solution():
    """Mary is counting the number of minnows in the pond. 40% of the minnows have red bellies, 30% have green bellies and the rest have white bellies. If 20 minnows have red bellies, how many minnows have white bellies?"""
    # Define the percentage of minnows with each type of belly
    RED_PERCENT = 0.4
    GREEN_PERCENT = 0.3

    # Calculate the total percentage of minnows with red or green bellies
    red_and_green_percent = RED_PERCENT + GREEN_PERCENT

    # Calculate the percentage of minnows with white bellies
    white_percent = 1 - red_and_green_percent

    # Calculate the total number of minnows
    red_count = 20
    total_count = red_count / RED_PERCENT

    # Calculate the number of minnows with white bellies
    white_count = int(total_count * white_percent)

    # Display the number of minnows with white bellies
    result = white_count
    return result

print(solution())