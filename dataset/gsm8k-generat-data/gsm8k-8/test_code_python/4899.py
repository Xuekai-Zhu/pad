def solution():
    # Define the name of Robin's friends
    friends = ['Jessica', 'Tori', 'Lily', 'Patrice']

    # Calculate the total number of bracelets needed
    total_bracelets = sum([len(friend) for friend in friends])

    # Calculate the total cost
    total_cost = total_bracelets * 2
    result = total_cost
    return result

print(solution())