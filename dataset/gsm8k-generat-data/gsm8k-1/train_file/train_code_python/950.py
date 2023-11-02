def solution():
    """Michonne is inviting her friends to her birthday party. She invites 6 of her friends from school and 12 of her friends from her neighborhood. Each of her friends asks if they can bring two friends along as well. How many people are going to Michonne’s birthday party?"""
    friends_from_school = 6
    friends_from_neighborhood = 12
    new_friends_per_person = 2
    total_people = friends_from_school + friends_from_neighborhood + (friends_from_school + friends_from_neighborhood) * new_friends_per_person
    result = total_people
    return result

print(solution())