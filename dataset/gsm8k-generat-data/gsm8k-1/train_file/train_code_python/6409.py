def solution():
    """Moore's family compared mobile phone plans to get the best deal. At T-Mobile, the family plan costs $50 per month for the first two lines and $16 for each additional line. At M-Mobile, the family plan costs $45 for the first two lines and $14 for each additional line. Moore's family needs to purchase 5 cell phone lines. How much cheaper is the M-Mobile than T-Mobile?"""
    tmobile_first_two_lines = 50
    tmobile_additional_lines = 16
    mmobile_first_two_lines = 45
    mmobile_additional_lines = 14
    total_lines = 5
    tmobile_cost = tmobile_first_two_lines + (total_lines - 2) * tmobile_additional_lines
    mmobile_cost = mmobile_first_two_lines + (total_lines - 2) * mmobile_additional_lines
    difference = tmobile_cost - mmobile_cost
    result = difference
    return result

print(solution())