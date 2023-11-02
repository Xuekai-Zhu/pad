def solution():
    # Define the number of pencils Sarah buys each day
    monday_pencils = 20
    tuesday_pencils = 18
    wednesday_pencils = 3 * tuesday_pencils

    # Calculate the total number of pencils Sarah has
    total_pencils = monday_pencils + tuesday_pencils + wednesday_pencils
    result = total_pencils
    return result

print(solution())