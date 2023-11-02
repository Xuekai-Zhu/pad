def solution():
    """Allie's making guacamole for a party. Each batch requires 4 avocados and serves about 6 people. If 42 people are going to be at the party including her, how many avocados does she need?"""
    # Define the number of people attending the party, including Allie
    num_people = 42

    # Calculate the number of batches needed to serve everyone
    num_batches = (num_people - 1) // 6 + 1

    # Calculate the total number of avocados needed
    num_avocados = num_batches * 4

    # return the result
    result = num_avocados
    return result

print(solution())