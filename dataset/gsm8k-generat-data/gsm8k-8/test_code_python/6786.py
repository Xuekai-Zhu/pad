def solution():
    # Define the initial length of Sandy's nails and the world record length
    sandy_length = 2
    record_length = 26

    # Calculate how many months Sandy will need to reach the record length
    months_to_record = (record_length - sandy_length) / 0.1

    # Convert the number of months to years and add to Sandy's age
    age_at_record = 12 + (months_to_record / 12)
    result = age_at_record
    return result

print(solution())