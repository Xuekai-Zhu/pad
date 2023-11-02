def solution():
    # Define the total number of spelling badges and the number of badges Hermione and Luna have
    total_badges = 83
    hermione_badges = 14
    luna_badges = 17

    # Calculate the number of badges Celestia has
    celestia_badges = total_badges - hermione_badges - luna_badges
    result = celestia_badges
    return result

print(solution())