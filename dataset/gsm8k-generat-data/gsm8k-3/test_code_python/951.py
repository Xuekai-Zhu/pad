def solution():
    """Michonne is inviting her friends to her birthday party. She invites 6 of her friends from school and 12 of her friends from her neighborhood. Each of her friends asks if they can bring two friends along as well. How many people are going to Michonne’s birthday party?"""
    # Define the number of friends Michonne invited
    school_friends = 6
    neighborhood_friends = 12

    # Calculate the number of additional friends each friend is bringing along
    additional_friends = 2

    # Calculate the total number of people coming to the party
    total_people = 1 + school_friends + neighborhood_friends + (school_friends + neighborhood_friends) * additional_friends

    # Display the total number of people
    result = total_people
    return result

print(solution())