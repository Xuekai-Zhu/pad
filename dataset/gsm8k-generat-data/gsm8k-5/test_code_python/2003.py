def solution():
    shoppers = 375  # There will be 375 shoppers
    yam_buyers = shoppers // 3  # Every third shopper buys a package of candied yams
    yam_packages = yam_buyers  # Each buyer buys one package of candied yams
    bulk_boxes = yam_packages // 25  # The store buys them in bulk boxes of 25 packages

    result = bulk_boxes
    return result

print(solution())