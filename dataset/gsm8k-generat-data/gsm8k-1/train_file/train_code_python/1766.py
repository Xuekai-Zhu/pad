def solution():
    """Juvy has a garden that has 20 rows with 10 plants in each row. She plants parsley in the first 3 rows and rosemary in the last two rows. The rest of the rows will be planted with chives. How many chives will Juvy plant?"""
    total_rows = 20
    parsley_rows = 3
    rosemary_rows = 2
    chive_rows = total_rows - parsley_rows - rosemary_rows
    plants_per_row = 10
    chives_planted = chive_rows * plants_per_row
    result = chives_planted
    return result

print(solution())