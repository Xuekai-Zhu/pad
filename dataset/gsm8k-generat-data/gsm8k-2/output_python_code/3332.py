def solution():
    """Roberta started off with 8 vinyl records. Her friends gave her 12 records for her birthday and she bought 30 more at a garage sale. It takes her 2 days to listen to 1 record. How many days will it take her to listen to her record collection?"""
    initial_records = 8
    birthday_records = 12
    garage_sale_records = 30
    total_records = initial_records + birthday_records + garage_sale_records
    listening_time_per_record = 2
    total_listening_time = total_records * listening_time_per_record
    result = total_listening_time
    return result/2 # return in days, not in units of 2-day periods.

print(solution())