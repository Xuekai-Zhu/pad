def solution():
    """Michonne is inviting her friends to her birthday party. She invites 6 of her friends from school and 12 of her friends from her neighborhood. Each of her friends asks if they can bring two friends along as well. How many people are going to Michonne’s birthday party?"""
    school_friends = 6
    neighborhood_friends = 12
    additional_friends = (school_friends + neighborhood_friends) * 2
    total_guests = school_friends + neighborhood_friends + additional_friends
    result = total_guests
    return result

print(solution())