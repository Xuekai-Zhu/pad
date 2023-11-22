def solution():
    
    # Define the number of adult's bowls and child's bowls
    adult_bowls = 4
    child_bowls = 8

    # Define the number of people in the pot
    num_people = 4 + 2

    # Calculate the total number of bowls in the pot
    total_bowls = adult_bowls + child_bowls

    # Calculate the number of bowls each child can have for lunch
    bowls_per_child = total_bowls // num_people

    # Display the number of times each child can have a bowl of soup for lunch
    result = bowls_per_child
    return result

print(solution())