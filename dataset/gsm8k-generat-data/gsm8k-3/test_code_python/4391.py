def solution():
    """Libby has 160 quarters in her piggy bank. She has to pay $35 to replace her sister’s dress that she borrowed and ruined. After replacing the dress, how many quarters will Libby have left?"""
    # Define the number of quarters Libby has
    quarters = 160

    # Define the cost of the dress replacement
    dress_cost = 35

    # Calculate the number of quarters needed for the dress replacement
    quarters_needed = dress_cost * 4

    # Calculate the number of quarters left after the dress replacement
    quarters_left = quarters - quarters_needed

    # Display the number of quarters left
    result = quarters_left
    return result

print(solution())