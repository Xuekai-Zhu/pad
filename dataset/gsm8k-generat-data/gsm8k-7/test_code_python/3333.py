def solution():
    initial_records = 8
    birthday_gifts = 12
    garage_sale = 30
    total_records = initial_records + birthday_gifts + garage_sale
    days_per_record = 2
    total_days = total_records * days_per_record
    result = total_days
    return result

print(solution())