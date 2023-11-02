def solution():
    """Ashley had a birthday party and invited 20 of her friends, telling them to each invite one more person to attend the party. If half the number of the invited guests each came with one more person, what's the total number of people at the party, including Ashley?"""
    # Define the initial number of guests Ashley invited
    initial_guests = 20

    # Calculate the number of guests each invited
    additional_guests = 1

    # Calculate the total number of guests after Ashley's friends each invite another person
    total_guests = initial_guests + (initial_guests * additional_guests)

    # Calculate the number of guests that came with an additional person
    guests_with_additional = total_guests * 0.5

    # Calculate the final total number of guests, including Ashley
    final_total = total_guests + guests_with_additional + 1

    # Return the result
    result = final_total
    return result

print(solution())