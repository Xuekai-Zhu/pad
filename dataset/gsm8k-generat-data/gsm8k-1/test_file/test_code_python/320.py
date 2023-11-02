def solution():
    """Ralph has a record store where people can trade their own records for new ones. People can trade 2 old records for 1 new one. 5 people come in with old records and leave with 7 new records between them. How many old records did the 5 people bring in?"""
    new_records_received = 7
    old_records_needed = new_records_received * 2
    num_people = 5
    total_old_records = num_people * old_records_needed
    result = total_old_records
    return result

print(solution())