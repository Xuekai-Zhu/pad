def solution():
    """Mrs. Amaro has 80 roses in her garden. Three-fourths of her roses are red, one-fourth of the remaining are yellow, and the rest are white. How many of Mrs. Amaro's roses are either red or white?"""
    # Calculate the number of red roses
    red_roses = 80 * 0.75

    # Calculate the number of remaining roses
    remaining_roses = 80 - red_roses

    # Calculate the number of yellow roses
    yellow_roses = remaining_roses * 0.25

    # Calculate the number of white roses
    white_roses = remaining_roses - yellow_roses

    # Calculate the total number of red or white roses
    total_roses = red_roses + white_roses

    # Display the total number of red or white roses
    result = total_roses
    return result

print(solution())