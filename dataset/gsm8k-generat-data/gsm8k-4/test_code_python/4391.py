def solution():
    """Libby has 160 quarters in her piggy bank. She has to pay $35 to replace her sister’s dress that she borrowed and ruined. After replacing the dress, how many quarters will Libby have left?"""
    # Define the initial number of quarters and the cost of the dress
    initial_quarters = 160
    dress_cost = 35

    # Calculate the number of quarters needed to pay for the dress
    quarters_needed = dress_cost / 0.25

    # Calculate the number of quarters that will be left
    quarters_left = initial_quarters - quarters_needed

    # Return the result
    result = quarters_left
    return result

print(solution())