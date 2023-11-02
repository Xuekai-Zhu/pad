def solution():
    initial_guests = 20  # Ashley invited 20 friends
    invited_per_guest = 1  # Each invited guest was told to bring one more person
    half_invited_guests = initial_guests * invited_per_guest / 2  # Half of the invited guests brought one more person

    # Calculate the total number of people at the party
    total_guests = initial_guests + half_invited_guests
    result = total_guests
    return result

print(solution())