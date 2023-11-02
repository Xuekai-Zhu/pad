def solution():
    """Candice put 80 post-it notes in her purse before she headed out to her job at the coffee shop. On her way, she stopped off at the store and purchased a package of Post-it notes; At work, she placed a single Post-it note on each of 220 different cups of coffee. If she had 23 post-it notes remaining overall, how many Post-it notes were in the package that she purchased?"""
    starting_notes = 80
    cups_of_coffee = 220
    remaining_notes = 23
    package_notes = cups_of_coffee + starting_notes - remaining_notes
    result = package_notes
    return result

print(solution())