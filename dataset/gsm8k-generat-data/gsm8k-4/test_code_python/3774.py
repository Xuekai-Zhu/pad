def solution():
    """Oliver has two bags of vegetables. Each bag weighs 1/6 as much as James’s bag, which weighs 18kg. What is the combined weight of both Oliver’s bags?"""
    # Define James's bag weight
    james_weight = 18

    # Calculate Oliver's bag weight
    oliver_weight = james_weight * (1/6)

    # Calculate the combined weight of both Oliver's bags
    combined_weight = oliver_weight * 2

    # Return the result
    result = combined_weight
    return result

print(solution())