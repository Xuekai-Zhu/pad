def solution():
    """Deborah has four letters to mail. Standard postage is $1.08 per letter, with an additional charge for international mail. Deborah is mailing two letters internationally, and she is paying $4.60 to mail four letters. How many cents is the additional charge per letter for international shipping?"""
    total_cost = 4.6
    standard_cost = 1.08
    international_letters = 2
    domestic_letters = 4 - international_letters
    international_cost = total_cost - (domestic_letters * standard_cost)
    international_charge_per_letter = international_cost / international_letters
    result = international_charge_per_letter * 100
    return result

print(solution())