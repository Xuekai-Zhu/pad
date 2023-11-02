def solution():
    """ Octavia wants to make a quilt for her sister. She is going to build it from small, medium, and large t-shirts that her family is done with. A small t-shirt is 3 square feet of fabric. A medium one is 4 square feet. A large one is 6 square feet. If she uses 11 small shirts, 8 medium, and 6 large shirts, how many square feet is the quilt?"""
    small_shirt_sqft = 3
    medium_shirt_sqft = 4
    large_shirt_sqft = 6
    num_small_shirts = 11
    num_medium_shirts = 8
    num_large_shirts = 6
    total_sqft = (small_shirt_sqft*num_small_shirts) + (medium_shirt_sqft*num_medium_shirts) + (large_shirt_sqft*num_large_shirts)
    result = total_sqft
    return result

print(solution())