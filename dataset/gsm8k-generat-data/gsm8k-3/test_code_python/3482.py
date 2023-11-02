def solution():
    """Cersei bought 50 cotton candies. She gave her brother and sister 5 cotton candies each, then gave the remaining one-fourth of them to her cousin. If she ate 12 cotton candies, how many cotton candies are left?"""
    # Define the total number of cotton candies bought
    total_cotton_candies = 50

    # Subtract the cotton candies given to her brother and sister
    total_cotton_candies -= 5 + 5

    # Calculate the number of cotton candies remaining after Cersei gave one-fourth to her cousin
    remaining_cotton_candies = total_cotton_candies * 3 / 4

    # Subtract the cotton candies Cersei ate
    remaining_cotton_candies -= 12

    # Display the number of cotton candies remaining
    result = remaining_cotton_candies
    return result

print(solution())