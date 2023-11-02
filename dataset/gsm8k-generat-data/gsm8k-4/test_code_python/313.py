def solution():
    """Hash has nine more than half as many toys as Bill has. If Bill has 60 toys, how many total toys do the boys have?"""
    # Define the number of toys Bill has
    bill_toys = 60

    # Calculate the number of toys Hash has
    hash_toys = (bill_toys / 2) + 9

    # Calculate the total number of toys the boys have
    total_toys = bill_toys + hash_toys

    # return the result
    result = total_toys
    return result

print(solution())