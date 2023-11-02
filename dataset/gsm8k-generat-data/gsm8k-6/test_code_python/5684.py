def solution():
    # Calculate the total number of kindergartners
    total_kids = 9 + 10 + 11

    # Calculate the total number of mini tissue boxes needed
    total_boxes = total_kids * 1  # each child needs one mini tissue box

    # Calculate the total number of tissues
    total_tissues = total_boxes * 40  # each mini tissue box contains 40 tissues

    result = total_tissues
    return result

print(solution())