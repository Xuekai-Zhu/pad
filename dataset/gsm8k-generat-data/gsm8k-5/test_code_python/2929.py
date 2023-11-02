def solution():
    total_badges = 83  # Total number of spelling badges the three girls have combined
    hermione_badges = 14  # Number of spelling badges Hermione has
    luna_badges = 17  # Number of spelling badges Luna has

    # Calculate the number of spelling badges Celestia has
    celestia_badges = total_badges - hermione_badges - luna_badges
    result = celestia_badges
    return result

print(solution())