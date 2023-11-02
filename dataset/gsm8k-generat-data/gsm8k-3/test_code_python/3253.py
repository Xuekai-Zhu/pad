def solution():
    """At the feline sanctuary, there were 12 lions, 14 tigers, and several cougars.  If there were half as many cougars as lions and tigers combined, then what was the total number of big cats at the feline sanctuary?"""
    # Calculate the total number of lions and tigers
    total_lions_tigers = 12 + 14

    # Calculate the number of cougars
    cougars = total_lions_tigers / 2

    # Calculate the total number of big cats
    total_big_cats = 12 + 14 + cougars

    # Display the total number of big cats
    result = total_big_cats
    return result

print(solution())