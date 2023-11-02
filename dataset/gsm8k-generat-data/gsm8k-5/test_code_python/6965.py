def solution():
    sheets_per_package = 250  # Each package contains 250 sheets of paper
    packages_per_box = 5  # Each box contains 5 packages of paper
    boxes = 2  # Julie bought 2 boxes of paper
    total_sheets = sheets_per_package * packages_per_box * boxes  # Calculate the total number of sheets of paper
    sheets_per_newspaper = 25  # Each newspaper uses 25 sheets of paper
    total_newspapers = total_sheets // sheets_per_newspaper  # Calculate the total number of newspapers that can be printed
    result = total_newspapers
    return result

print(solution())