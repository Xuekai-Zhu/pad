def solution():
    num_boxes = 2
    num_packages_per_box = 5
    num_sheets_per_package = 250
    num_sheets_per_newspaper = 25

    # Calculate the total number of sheets of paper that Julie purchased
    total_sheets_purchased = num_boxes * num_packages_per_box * num_sheets_per_package

    # Calculate the total number of newspapers that Julie can print
    num_newspapers = total_sheets_purchased // num_sheets_per_newspaper

    result = num_newspapers
    return result

print(solution())