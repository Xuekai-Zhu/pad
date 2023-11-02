def solution():
    """At the feline sanctuary, there were 12 lions, 14 tigers, and several cougars. If there were half as many cougars as lions and tigers combined, then what was the total number of big cats at the feline sanctuary?"""
    # Define the number of lions and tigers
    lions = 12
    tigers = 14

    # Calculate the combined number of lions and tigers
    lions_and_tigers = lions + tigers

    # Calculate the number of cougars
    cougars = lions_and_tigers / 2

    # Calculate the total number of big cats
    total_cats = lions + tigers + cougars

    result = total_cats
    return result

print(solution())