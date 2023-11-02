def solution():
    """Erika and her 3 siblings are drawing with chalk outside. Another 3 friends join them and ask if they can help with the drawing. Erika loses 2 pieces of chalk as they are counting and the group realizes there isn't enough chalk for everyone. Erika’s mom brings out another 12 pieces of chalk for them to share and there is now enough chalk for everyone to have 3 pieces each. How many pieces of chalk did Erika and her siblings originally have?"""
    initial_chalk = (4 * 3) - 2  # Erika and her 3 siblings had 3 pieces each, minus the 2 lost pieces
    total_people = 7  # Erika, her siblings, and 3 friends
    total_chalk = initial_chalk + 12  # Erika's mom brought out 12 more pieces
    remaining_chalk = total_chalk - (total_people * 3)  # Each person now has 3 pieces, so subtract from total
    result = initial_chalk
    return result

print(solution())