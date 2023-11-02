def solution():
    """Erika and her 3 siblings are drawing with chalk outside. Another 3 friends join them and ask if they can help with the drawing.
    Erika loses 2 pieces of chalk as they are counting and the group realizes there isn't enough chalk for everyone.
    Erika’s mom brings out another 12 pieces of chalk for them to share and there is now enough chalk for everyone to have 3 pieces each.
    How many pieces of chalk did Erika and her siblings originally have?"""
    
    siblings = 4
    friends = 3
    total_people = siblings + friends
    
    initial_chalk = (total_people * 3) - 12
    
    # Subtracting the 2 pieces that Erika lost
    initial_chalk -= 2
    
    result = initial_chalk
    return result

print(solution())