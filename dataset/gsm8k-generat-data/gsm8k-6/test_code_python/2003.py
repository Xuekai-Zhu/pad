def solution():
    # Calculate the number of packages of candied yams the store needs to order
    packages_needed = 375 // 3  # every third shopper buys a package
    boxes_needed = packages_needed // 25  # 25 packages per bulk box
    if packages_needed % 25 != 0:  # if there are leftover packages, add another box
        boxes_needed += 1
    result = boxes_needed
    return result

print(solution())