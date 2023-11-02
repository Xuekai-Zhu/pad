def solution():
    """Ali has a small flower shop. He sold 4 flowers on Monday, 8 flowers on Tuesday and on Friday, he sold double the number of flowers he sold on Monday. How many flowers does Ali sell?"""
    # Calculate the number of flowers sold on Monday and Tuesday
    monday_flowers = 4
    tuesday_flowers = 8

    # Calculate the number of flowers sold on Friday
    friday_flowers = monday_flowers * 2

    # Calculate the total number of flowers sold
    total_flowers = monday_flowers + tuesday_flowers + friday_flowers

    # return the result
    result = total_flowers
    return result

print(solution())