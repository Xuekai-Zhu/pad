def solution():
    """Erika and her 3 siblings are drawing with chalk outside. Another 3 friends join them and ask if they can help with the drawing. Erika loses 2 pieces of chalk as they are counting and the group realizes there isn't enough chalk for everyone. Erika’s mom brings out another 12 pieces of chalk for them to share and there is now enough chalk for everyone to have 3 pieces each. How many pieces of chalk did Erika and her siblings originally have?"""
    
    # Define the initial number of chalk pieces
    initial_chalk = None

    # Define the number of people drawing
    total_people = 7

    # Define the number of chalk pieces lost
    lost_chalk = 2

    # Define the number of extra chalk pieces added
    extra_chalk = 12

    # Define the final number of chalk pieces per person
    final_chalk_per_person = 3

    # Calculate the total number of chalk pieces after Erika's mom adds more
    total_chalk = final_chalk_per_person * total_people - extra_chalk

    # Calculate the initial number of chalk pieces
    initial_chalk = total_chalk + lost_chalk

    result = initial_chalk
    return result

print(solution())