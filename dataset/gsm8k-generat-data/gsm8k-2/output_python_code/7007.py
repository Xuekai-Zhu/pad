def solution():
    """Davonte is trying to figure out how much space his art collection takes up. He measures his paintings and finds he has three square 6-foot by 6-foot paintings, four small 2-foot by 3-foot paintings, and one large 10-foot by 15-foot painting. How many square feet does his collection take up?"""
    square_paintings = 3 * 6 * 6
    small_paintings = 4 * 2 * 3
    large_painting = 10 * 15
    total_square_feet = square_paintings + small_paintings + large_painting
    result = total_square_feet
    return result

print(solution())