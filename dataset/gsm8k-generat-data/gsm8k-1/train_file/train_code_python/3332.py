def solution():
    """Roberta started off with 8 vinyl records. Her friends gave her 12 records for her birthday and she bought 30 more at a garage sale. It takes her 2 days to listen to 1 record. How many days will it take her to listen to her record collection?"""
    initial_records = 8
    birthday_records = 12
    garage_sale_records = 30
    total_records = initial_records + birthday_records + garage_sale_records
    days_per_record = 2
    total_days = total_records * days_per_record
    result = total_days
    return result

print(solution())