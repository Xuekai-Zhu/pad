def solution():
    """Juvy has a garden that has 20 rows with 10 plants in each row. She plants parsley in the first 3 rows and rosemary in the last two rows. The rest of the rows will be planted with chives. How many chives will Juvy plant?"""
    # Define the number of rows planted with parsley and rosemary
    parsley_rows = 3
    rosemary_rows = 2

    # Calculate the total number of rows planted with parsley and rosemary
    herb_rows = parsley_rows + rosemary_rows

    # Calculate the total number of chive rows
    chive_rows = 20 - herb_rows

    # Calculate the total number of chives
    chive_plants = chive_rows * 10

    # Display the total number of chives
    result = chive_plants
    return result

print(solution())