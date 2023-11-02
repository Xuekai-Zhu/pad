def solution():
    """Roberta started off with 8 vinyl records. Her friends gave her 12 records for her birthday and she bought 30 more at a garage sale. It takes her 2 days to listen to 1 record. How many days will it take her to listen to her record collection?"""
    # Define the initial number of vinyl records
    vinyl_records = 8

    # Add the number of vinyl records she received as gifts
    vinyl_records += 12

    # Add the number of vinyl records she bought at the garage sale
    vinyl_records += 30

    # Calculate the total number of days it will take her to listen to all of the vinyl records
    total_days = vinyl_records * 2

    # return the result
    result = total_days
    return result

print(solution())