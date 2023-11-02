def solution():
    """Kira's cat eats a pound of kibble every 4 hours. Kira fills her cat's bowl with 3 pounds of kibble before going to work. When she returns, Kira weighs the bowl and there is still 1 pound left. How many hours was Kira away from home?"""
    kibble_per_hour = 1/4
    initial_kibble = 3
    remaining_kibble = 1
    hours_of_absence = (initial_kibble - remaining_kibble) / kibble_per_hour
    result = hours_of_absence
    return result

print(solution())