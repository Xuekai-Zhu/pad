def solution():
    initial_records = 8  # Roberta starts with 8 records
    records_from_friends = 12  # Roberta receives 12 records from friends
    records_from_garage_sale = 30  # Roberta buys 30 records at a garage sale
    total_records = initial_records + records_from_friends + records_from_garage_sale  # Roberta has a total of these records
    days_per_record = 2  # Roberta takes 2 days to listen to 1 record

    # Calculate the total number of days it will take Roberta to listen to her entire record collection
    total_days = total_records * days_per_record
    result = total_days
    return result

print(solution())