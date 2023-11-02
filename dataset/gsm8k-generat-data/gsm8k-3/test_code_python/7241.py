def solution():
    """Claire has 400 flowers in her garden. One hundred twenty are tulips, and the rest are roses. Eighty of the roses are white, while the rest are red. Each red rose is worth $0.75. How much will Claire earn if she can sell 1/2 of the total number of red roses?"""
    # Define the number of tulips and white roses in Claire's garden
    tulips = 120
    white_roses = 80

    # Calculate the number of red roses in Claire's garden
    red_roses = 400 - tulips - white_roses

    # Calculate the total earnings if Claire sells half of the red roses
    earnings = (red_roses / 2) * 0.75

    # Display the total earnings
    result = earnings
    return result

print(solution())