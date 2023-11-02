def solution():
    """At a cafe, the breakfast plate has two eggs and twice as many bacon strips as eggs.  If 14 customers order breakfast plates, how many bacon strips does the cook need to fry?"""
    # Define the number of eggs per plate and the ratio of bacon strips to eggs
    EGGS_PER_PLATE = 2
    BACON_PER_EGG = 2

    # Define the number of plates ordered
    plates_ordered = 14

    # Calculate the total number of eggs needed
    eggs_needed = plates_ordered * EGGS_PER_PLATE

    # Calculate the total number of bacon strips needed
    bacon_needed = eggs_needed * BACON_PER_EGG

    # Display the total number of bacon strips needed
    result = bacon_needed
    return result

print(solution())