def solution():
    # Define the initial number of records
    initial_records = 8

    # Define the additional records
    birthday_records = 12
    garage_sale_records = 30

    # Calculate the total number of records
    total_records = initial_records + birthday_records + garage_sale_records

    # Calculate the number of days to listen to all the records
    days_to_listen = total_records * 2

    result = days_to_listen
    return result

print(solution())