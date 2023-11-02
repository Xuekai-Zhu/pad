def solution():
    """Ali has a small flower shop. He sold 4 flowers on Monday, 8 flowers on Tuesday and on Friday, he sold double the number of flowers he sold on Monday. How many flowers does Ali sell?"""
    flowers_monday = 4
    flowers_tuesday = 8
    flowers_friday = flowers_monday * 2
    total_flowers = flowers_monday + flowers_tuesday + flowers_friday
    result = total_flowers
    return result

print(solution())