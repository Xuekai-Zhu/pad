def solution():
    total_collection = 2000
    school_population = 400
    num_attendees = school_population / 2

    # Calculate the collection per person at the party
    collection_per_person = total_collection / num_attendees

    # Calculate the collection if 300 people attended
    collection_with_300_attendees = collection_per_person * 300
    result = collection_with_300_attendees
    return result

print(solution())