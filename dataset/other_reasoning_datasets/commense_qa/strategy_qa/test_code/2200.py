def solution():
    # Define the relationship between Adam and Eve
    eve_made_from_adam = True
    siblings_have_similar_DNA = True
    starting_family_together = True
    # Check if Eve was involved in an incestuous relationship
    if eve_made_from_adam and siblings_have_similar_DNA and starting_family_together:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())