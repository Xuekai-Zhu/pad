def solution():
    # Define the location of the Statue of Freedom and the Statue of Liberty
    statue_of_freedom_location = "Washington, D.C."
    statue_of_liberty_location = "New York City"
    # Check if the two statues are in the same line of sight
    if statue_of_freedom_location != statue_of_liberty_location:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())