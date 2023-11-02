def solution():
    
    # Define the number of boxes and crayons per box
    boxes = 3
    crayons_per_box = 64

    # Calculate the total number of small pieces of crayons
    total_small_pieces = boxes * crayons_per_box

    # Calculate the total number of muffin crayons
    total_muffin_crayons = total_small_pieces * 8

    # Calculate the total amount of money Kate can make
    total_money = total_muffin_crayons * 1.5

    # return the result
    result = total_money
    return result

print(solution())