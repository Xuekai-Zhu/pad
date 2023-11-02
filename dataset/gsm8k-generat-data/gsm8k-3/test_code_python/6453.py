def solution():
    """Allie's making guacamole for a party. Each batch requires 4 avocados and serves about 6 people. If 42 people are going to be at the party including her, how many avocados does she need?"""
    # Define the number of people per batch
    PEOPLE_PER_BATCH = 6

    # Define the number of people at the party
    party_size = 42

    # Calculate the number of batches needed
    batches_needed = (party_size - 1) // PEOPLE_PER_BATCH + 1

    # Calculate the number of avocados needed
    avocados_needed = batches_needed * 4

    # Display the number of avocados needed
    result = avocados_needed
    return result

print(solution())