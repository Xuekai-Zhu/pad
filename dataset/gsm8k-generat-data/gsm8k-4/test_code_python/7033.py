def solution():
    """A group of security guards were hired for the night shift at a factory. The four guards agreed to a rotating schedule to cover the nine hours of the night shift. The first guard would take three hours since they were still awake, the last guard would wake up early and take two hours, and the middle two guards would split the remaining hours. How many hours will each middle guard take?"""
    # Define the total number of hours in the night shift
    total_hours = 9

    # Define the number of hours the first guard will work
    first_guard_hours = 3

    # Define the number of hours the last guard will work
    last_guard_hours = 2

    # Calculate the remaining hours
    remaining_hours = total_hours - first_guard_hours - last_guard_hours

    # Divide the remaining hours between the two middle guards
    middle_guards_hours = remaining_hours / 2

    result = middle_guards_hours
    return result

print(solution())