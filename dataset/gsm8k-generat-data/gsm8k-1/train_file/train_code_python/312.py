def solution():
    """Hash has nine more than half as many toys as Bill has. If Bill has 60 toys, how many total toys do the boys have?"""
    bill_toys = 60
    hash_toys = (bill_toys / 2) + 9
    total_toys = bill_toys + hash_toys
    result = total_toys
    return result

print(solution())