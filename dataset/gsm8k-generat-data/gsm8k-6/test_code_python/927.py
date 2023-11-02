def solution():
    # Calculate the number of people invited by Ashley's friends
    friend_invitations = 20 * 1  # each of the 20 friends invited one more person

    # Calculate the number of people who came with Ashley's friends
    extra_people = (friend_invitations / 2) * 1  # half of the invited guests came with one more person

    # Calculate the total number of people at the party
    total_people = 1 + 20 + friend_invitations + extra_people  # Ashley + her 20 friends + invited guests + extra people

    result = total_people
    return result

print(solution())