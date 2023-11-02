def solution():
    """A group of security guards were hired for the night shift at a factory. The four guards agreed to a rotating schedule to cover the nine hours of the night shift. The first guard would take three hours since they were still awake, the last guard would wake up early and take two hours, and the middle two guards would split the remaining hours. How many hours will each middle guard take?"""
    total_hours = 9
    first_guard_hours = 3
    last_guard_hours = 2
    middle_guards_hours = total_hours - first_guard_hours - last_guard_hours
    middle_guard_hours_each = middle_guards_hours / 2
    result = middle_guard_hours_each
    return result

print(solution())