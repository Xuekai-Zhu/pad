def solution():
    """Candied yams fly off the shelf during the holiday season. The store buys them in bulk boxes of 25 packages. If every third shopper buys a package of candied yams, how many bulk boxes of candied yams will the store need to order for their 375 predicted holiday shoppers?"""
    # Calculate the number of shoppers expected to buy candied yams
    yam_shoppers = 375 // 3

    # Calculate the number of packages of yams needed
    yam_packages = yam_shoppers

    # Calculate the number of bulk boxes needed
    bulk_boxes = yam_packages // 25 + (yam_packages % 25 > 0)

    # return the result
    result = bulk_boxes
    return result

print(solution())