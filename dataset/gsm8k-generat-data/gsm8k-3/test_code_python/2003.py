def solution():
    """Candied yams fly off the shelf during the holiday season. The store buys them in bulk boxes of 25 packages. If every third shopper buys a package of candied yams, how many bulk boxes of candied yams will the store need to order for their 375 predicted holiday shoppers?"""
    # Find the number of shoppers that will buy candied yams
    yam_shoppers = 375 // 3

    # Find the number of packages of yams needed
    yam_packages = yam_shoppers

    # Find the number of bulk boxes needed
    boxes_needed = yam_packages // 25 + (1 if yam_packages % 25 != 0 else 0)

    # Display the number of boxes needed
    result = boxes_needed
    return result

print(solution())