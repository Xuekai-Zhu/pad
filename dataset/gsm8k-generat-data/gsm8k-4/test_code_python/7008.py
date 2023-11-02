def solution():
    """Davonte is trying to figure out how much space his art collection takes up. He measures his paintings and finds he has three square 6-foot by 6-foot paintings, four small 2-foot by 3-foot paintings, and one large 10-foot by 15-foot painting. How many square feet does his collection take up?"""
    # Calculate the total square footage of the three square paintings
    square_paintings_area = 3 * 6 * 6

    # Calculate the total square footage of the four small paintings
    small_paintings_area = 4 * 2 * 3

    # Calculate the total square footage of the large painting
    large_painting_area = 10 * 15

    # Calculate the total square footage of the art collection
    total_area = square_paintings_area + small_paintings_area + large_painting_area

    result = total_area
    return result

print(solution())