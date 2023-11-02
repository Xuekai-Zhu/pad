def solution():
    """Javier has a wife and 3 children. They have 2 dogs and 1 cat. Including Javier, how many legs are there in total in Javier's household?"""
    # Define the number of legs for each member of the household
    JAVIER_LEGS = 2
    WIFE_LEGS = 2
    CHILD_LEGS = 2
    DOG_LEGS = 4
    CAT_LEGS = 4

    # Define the number of each member in the household
    num_javier = 1
    num_wife = 1
    num_children = 3
    num_dogs = 2
    num_cat = 1

    # Calculate the total number of legs in the household
    total_legs = (num_javier * JAVIER_LEGS) + (num_wife * WIFE_LEGS) + (num_children * CHILD_LEGS) + (num_dogs * DOG_LEGS) + (num_cat * CAT_LEGS)

    # Display the total number of legs
    result = total_legs
    return result

print(solution())