def solution():
    """Candied yams fly off the shelf during the holiday season. The store buys them in bulk boxes of 25 packages. If every third shopper buys a package of candied yams, how many bulk boxes of candied yams will the store need to order for their 375 predicted holiday shoppers?"""
    packages_per_box = 25
    shoppers_per_package = 3
    predicted_shoppers = 375
    total_packages = predicted_shoppers / shoppers_per_package
    total_boxes = total_packages / packages_per_box
    result = round(total_boxes)
    return result

print(solution())