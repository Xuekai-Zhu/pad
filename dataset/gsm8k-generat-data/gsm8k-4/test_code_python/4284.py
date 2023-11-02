def solution():
    """Jeff had 300 pencils and donated 30% of them. 
    Vicki had twice as many pencils as Jeff and donated 3/4 of his pencils. 
    How many pencils are there remaining altogether?"""
    # Define the initial number of pencils Jeff had
    jeff_pencils = 300

    # Calculate the number of pencils Jeff donated
    jeff_donated = jeff_pencils * 0.3

    # Calculate the number of pencils Jeff has left
    jeff_left = jeff_pencils - jeff_donated

    # Calculate the number of pencils Vicki has
    vicki_pencils = jeff_pencils * 2

    # Calculate the number of pencils Vicki donated
    vicki_donated = vicki_pencils * (3/4)

    # Calculate the number of pencils Vicki has left
    vicki_left = vicki_pencils - vicki_donated

    # Calculate the total number of pencils left
    total_left = jeff_left + vicki_left

    result = total_left
    return result

print(solution())