def solution():
    num_new_people = 2
    num_old_records_per_person = 2
    num_new_people = 7

    # Calculate the total number of new records
    total_new_records = num_new_people * num_old_records_per_person

    # Calculate the total number of old records
    total_old_records = total_new_records + num_old_records_per_person
    result = total_old_records
    return result

print(solution())