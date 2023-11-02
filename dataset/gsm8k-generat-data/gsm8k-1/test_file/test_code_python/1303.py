def solution():
    """James is putting together 4 tables. Each table has 4 legs and each leg needs 2 screws. He has 40 screws. How many screws will he have left over?"""
    tables_to_assemble = 4
    legs_per_table = 4
    screws_per_leg = 2
    total_screws_needed = tables_to_assemble * legs_per_table * screws_per_leg
    screws_leftover = 40 - total_screws_needed
    result = screws_leftover
    return result

print(solution())