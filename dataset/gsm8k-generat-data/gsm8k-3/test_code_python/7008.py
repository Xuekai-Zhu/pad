def solution():
    """Davonte is trying to figure out how much space his art collection takes up. He measures his paintings and finds he has three square 6-foot by 6-foot paintings, four small 2-foot by 3-foot paintings, and one large 10-foot by 15-foot painting. How many square feet does his collection take up?"""
    # Calculate the square footage of the three square paintings
    square_paintings = 3 * (6 * 6)

    # Calculate the square footage of the four small paintings
    small_paintings = 4 * (2 * 3)

    # Calculate the square footage of the large painting
    large_painting = 10 * 15

    # Calculate the total square footage of the collection
    total_square_footage = square_paintings + small_paintings + large_painting

    # Display the total square footage
    result = total_square_footage
    return result

print(solution())