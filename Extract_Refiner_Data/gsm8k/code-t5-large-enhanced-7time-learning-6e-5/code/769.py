def solution():
    
    # Define the initial number of pencils
    initial_pencils = 50

    # Calculate the number of pencils given to Brandon
    brandon_pencils = initial_pencils / 2

    # Calculate the number of pencils remaining after giving to Brandon
    remaining_pencils = initial_pencils - brandon_pencils

    # Calculate the number of pencils given to Charlie
    charlie_pencils = remaining_pencils * 3 / 5

    # Calculate the number of pencils remaining after giving to Charlie
    remaining_pencils = remaining_pencils - charlie_pencils

    # Display the number of pencils Anthony kept
    result = remaining_pencils
    return result

print(solution())