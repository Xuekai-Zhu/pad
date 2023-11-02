def solution():
    """Roberta started off with 8 vinyl records.  Her friends gave her 12 records for her birthday and she bought 30 more at a garage sale.  It takes her 2 days to listen to 1 record. How many days will it take her to listen to her record collection?"""
    # Define the number of records Roberta has
    num_records = 8 + 12 + 30

    # Calculate the total number of days it will take Roberta to listen to all her records
    total_days = num_records * 2

    # Display the total number of days
    result = total_days
    return result

print(solution())