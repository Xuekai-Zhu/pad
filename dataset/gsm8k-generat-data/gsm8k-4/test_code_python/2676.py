def solution():
    """Jennifer decides to share her sweets between herself and her 3 friends. She has 212 green sweets, 310 blue sweets and 502 yellow sweets. How many sweets will Jennifer and her friends get each?"""
    # Define the number of Jennifer's friends
    num_friends = 3

    # Calculate the total number of sweets
    total_sweets = 212 + 310 + 502

    # Calculate the number of sweets per person
    sweets_per_person = total_sweets // (num_friends + 1)

    # Return the result
    result = sweets_per_person
    return result

print(solution())