def solution():
    """Erika and her 3 siblings are drawing with chalk outside. Another 3 friends join them and ask if they can help with the drawing. Erika loses 2 pieces of chalk as they are counting and the group realizes there isn't enough chalk for everyone. Erika’s mom brings out another 12 pieces of chalk for them to share and there is now enough chalk for everyone to have 3 pieces each. How many pieces of chalk did Erika and her siblings originally have?"""
    # Define the number of people drawing before and after the friends join
    PEOPLE_BEFORE = 4
    PEOPLE_AFTER = 7

    # Define the number of pieces of chalk Erika loses and the number her mom brings
    LOST_CHALK = 2
    EXTRA_CHALK = 12

    # Define the desired number of chalk pieces per person
    DESIRED_CHALK = 3

    # Calculate the total number of chalk pieces needed
    total_needed = PEOPLE_AFTER * DESIRED_CHALK

    # Calculate the initial number of chalk pieces Erika and her siblings had
    initial_chalk = (total_needed - EXTRA_CHALK + LOST_CHALK) / PEOPLE_BEFORE

    # Display the initial number of chalk pieces
    result = initial_chalk
    return result

print(solution())