def solution():
    """Juvy has a garden that has 20 rows with 10 plants in each row. She plants parsley in the first 3 rows and rosemary in the last two rows. The rest of the rows will be planted with chives. How many chives will Juvy plant?"""
    # Define the number of rows and plants per row
    rows = 20
    plants_per_row = 10

    # Define the number of rows planted with parsley and rosemary
    parsley_rows = 3
    rosemary_rows = 2

    # Calculate the total number of parsley and rosemary plants
    parsley_plants = parsley_rows * plants_per_row
    rosemary_plants = rosemary_rows * plants_per_row

    # Calculate the total number of chive plants
    chive_plants = (rows * plants_per_row) - parsley_plants - rosemary_plants

    # return the result
    result = chive_plants
    return result

print(solution())