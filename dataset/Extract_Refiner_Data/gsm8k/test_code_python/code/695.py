def solution():
    
    # Define the total number of pencils and the number of missing pencils
    total_pencils = 20
    missing_pencils = 4

    # Calculate the number of pencils in the box
    pencils_in_box = total_pencils - missing_pencils

    # Calculate the number of pairs of pencils in the box
    pairs_in_box = pencils_in_box // 2

    # return the result
    result = pairs_in_box
    return result

print(solution())