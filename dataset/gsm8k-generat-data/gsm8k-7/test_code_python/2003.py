def solution():
    num_packages_per_box = 25
    num_shoppers = 375
    packages_per_shopper = 1/3 # Every third shopper buys a package

    # Calculate the total number of packages of candied yams that will be sold
    total_packages_sold = num_shoppers * packages_per_shopper

    # Calculate the total number of bulk boxes needed to hold all the packages
    total_boxes_needed = total_packages_sold / num_packages_per_box
    result = total_boxes_needed
    return result

print(solution())