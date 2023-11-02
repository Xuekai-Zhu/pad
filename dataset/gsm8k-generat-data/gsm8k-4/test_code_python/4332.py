def solution():
    """Bill and Jean are both cleaning out their garages. Bill makes a certain number of trips to the dump and Jean makes that many trips plus 6. If they make 40 trips total, how many trips does Jean make?"""
    # Define the number of trips Bill makes as x
    x = None

    # Set up an equation based on the information given
    x + (x+6) = 40

    # Solve for x
    x = 17

    # Calculate the number of trips Jean makes based on the value of x
    jean_trips = x + 6

    result = jean_trips
    return result

print(solution())