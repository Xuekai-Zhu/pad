def solution():
    
    # Define the number of new records per person
    NEW_RECORD_PER_PERSON = 2

    # Define the number of people who traded their records for
    num_people = 5

    # Calculate the total number of new records
    total_new_records = 7

    # Calculate the total number of records that the 5 people traded their records
    total_trades = num_people * NEW_RECORD_PER_PERSON

    # Calculate the total number of old records that the 5 people bring in
    total_old_records = total_trades * NEW_RECORD_PER_PERSON

    # Display the total number of old records
    result = total_old_records
    return result

print(solution())