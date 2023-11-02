def solution():
    """A group of security guards were hired for the night shift at a factory. The four guards agreed to a rotating schedule to cover the nine hours of the night shift. The first guard would take three hours since they were still awake, the last guard would wake up early and take two hours, and the middle two guards would split the remaining hours. How many hours will each middle guard take?"""
    # Define the total hours of the night shift
    total_hours = 9

    # Calculate the hours taken by the first guard
    first_guard_hours = 3

    # Calculate the hours taken by the last guard
    last_guard_hours = 2

    # Calculate the remaining hours
    remaining_hours = total_hours - first_guard_hours - last_guard_hours

    # Calculate the hours taken by each of the middle guards
    middle_guards_hours = remaining_hours / 2

    # Display the hours taken by each of the middle guards
    result = middle_guards_hours
    return result

print(solution())