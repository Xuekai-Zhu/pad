def solution():
    """Micah picks 2 dozen strawberries from the field. He eats 6 and saves the rest for his mom. How many strawberries are there for his mom?"""
    strawberries_per_dozen = 12
    total_strawberries = 2 * strawberries_per_dozen
    eaten_strawberries = 6
    strawberries_for_mom = total_strawberries - eaten_strawberries
    result = strawberries_for_mom
    return result

print(solution())