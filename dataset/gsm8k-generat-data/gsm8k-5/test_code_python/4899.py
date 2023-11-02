def solution():
    friends = ['Jessica', 'Tori', 'Lily', 'Patrice']  # Robin's friends
    total_bracelets = sum([len(name) for name in friends])  # Calculate the total number of bracelets needed
    cost_per_bracelet = 2  # Each jelly bracelet costs $2
    total_cost = total_bracelets * cost_per_bracelet  # Calculate the total cost of all the bracelets
    result = total_cost
    return result

print(solution())