def solution():
    """Selena and Josh were running in a race. Together they ran 36 miles. Josh ran half of the distance that Selena ran. How many miles did Selena run?"""
    # Define the total distance run
    total_distance = 36

    # Calculate the distance run by Josh
    josh_distance = total_distance / 3  # Since Josh ran half of the distance of Selena, the ratio between Josh and Selena distance is 1:2, which is 1/3 and 2/3 respectively

    # Calculate the distance run by Selena
    selena_distance = 2 * josh_distance

    # return the result
    result = selena_distance
    return result

print(solution())