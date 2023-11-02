def solution():
    """Candied yams fly off the shelf during the holiday season. The store buys them in bulk boxes of 25 packages. If every third shopper buys a package of candied yams, how many bulk boxes of candied yams will the store need to order for their 375 predicted holiday shoppers?"""
    shoppers = 375
    packages_per_shopper = 1 / 3
    total_packages = shoppers * packages_per_shopper
    boxes = total_packages / 25
    result = math.ceil(boxes)
    return result

print(solution())