def solution():
    """Hermione, Luna, and Celestia combined have 83 spelling badges. If Hermione has 14 and Luna has 17, how many spelling badges does Celestia have?"""
    # Define the total number of spelling badges
    total = 83

    # Define the number of spelling badges Hermione and Luna have combined
    hermione_luna = 14 + 17

    # Calculate the number of spelling badges Celestia has
    celestia = total - hermione_luna

    # return the result
    result = celestia
    return result

print(solution())