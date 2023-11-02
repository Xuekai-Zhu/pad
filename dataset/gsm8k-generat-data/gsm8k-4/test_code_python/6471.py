def solution():
    """Jemma saw 7 grasshoppers on her African daisy plant. Then, hopping on the grass under the plant, she found 2 dozen baby grasshoppers. How many grasshoppers did Jemma find altogether?"""
    # Define the number of grasshoppers Jemma saw on the plant
    grasshoppers_on_plant = 7

    # Define the number of dozen baby grasshoppers Jemma found on the grass
    dozen_baby_grasshoppers = 2

    # Convert the number of dozen baby grasshoppers to the total number of baby grasshoppers
    total_baby_grasshoppers = dozen_baby_grasshoppers * 12

    # Calculate the total number of grasshoppers Jemma found
    total_grasshoppers = grasshoppers_on_plant + total_baby_grasshoppers

    # Return the result
    result = total_grasshoppers
    return result

print(solution())