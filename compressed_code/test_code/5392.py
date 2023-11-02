def solution():
    
    sheets_per_package = 250
    packages_per_box = 5
    boxes = 2
    total_sheets = sheets_per_package * packages_per_box * boxes
    sheets_per_newspaper = 25
    newspapers_that_can_be_printed = total_sheets // sheets_per_newspaper
    result = newspapers_that_can_be_printed
    return result

print(solution())