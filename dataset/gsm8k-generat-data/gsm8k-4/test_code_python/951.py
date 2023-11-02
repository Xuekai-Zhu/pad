def solution():
    """Michonne is inviting her friends to her birthday party. She invites 6 of her friends from school and 12 of her friends from her neighborhood. Each of her friends asks if they can bring two friends along as well. How many people are going to Michonne’s birthday party?"""
    # Define the number of friends Michonne invited from school and her neighborhood
    school_friends = 6
    neighborhood_friends = 12

    # Calculate the total number of people invited to the party
    total_invited = school_friends + neighborhood_friends

    # Calculate the number of people each friend will bring along
    extra_people = 2

    # Calculate the total number of extra people
    total_extra_people = extra_people * total_invited

    # Add the extra people to the total number of invited people
    total_people = total_invited + total_extra_people

    # return the result
    result = total_people
    return result

print(solution())