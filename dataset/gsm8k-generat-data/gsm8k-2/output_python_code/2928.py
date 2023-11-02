def solution():
    """Hermione, Luna, and Celestia combined have 83 spelling badges. If Hermione has 14 and Luna has 17, how many spelling badges does Celestia have?"""
    total_badges = 83
    hermione_badges = 14
    luna_badges = 17
    celestia_badges = total_badges - hermione_badges - luna_badges
    result = celestia_badges
    return result

print(solution())