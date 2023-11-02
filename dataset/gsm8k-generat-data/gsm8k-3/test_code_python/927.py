def solution():
    """Ashley had a birthday party and invited 20 of her friends, telling them to each invite one more person to attend the party. If half the number of the invited guests each came with one more person, what's the total number of people at the party, including Ashley?"""
    # Define the number of friends Ashley invited
    num_friends = 20

    # Calculate the number of additional guests
    num_additional = num_friends * 1

    # Calculate the number of total guests from the added guests
    num_added = num_additional // 2

    # Calculate the total number of guests
    total_guests = num_friends + num_added + 1  # Add 1 for Ashley

    # Display the total number of guests
    result = total_guests
    return result

print(solution())