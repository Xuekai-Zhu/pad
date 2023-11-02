def solution():
    
    packages_per_box = 25
    shoppers_per_package = 3
    predicted_shoppers = 375
    total_packages = predicted_shoppers / shoppers_per_package
    total_boxes = total_packages / packages_per_box
    result = round(total_boxes)
    return result

print(solution())