def solution():
    """Claire has 400 flowers in her garden. One hundred twenty are tulips, and the rest are roses. Eighty of the roses are white, while the rest are red. Each red rose is worth $0.75. How much will Claire earn if she can sell 1/2 of the total number of red roses?"""
    # Define the total number of flowers and the number of tulips
    total_flowers = 400
    tulips = 120

    # Calculate the number of roses
    roses = total_flowers - tulips

    # Calculate the number of white roses
    white_roses = 80

    # Calculate the number of red roses
    red_roses = roses - white_roses

    # Calculate the total earnings from selling all the red roses
    total_earnings = red_roses * 0.75

    # Calculate the earnings from selling half of the red roses
    half_red_roses_earnings = (red_roses / 2) * 0.75

    # return the result
    result = half_red_roses_earnings
    return result

print(solution())