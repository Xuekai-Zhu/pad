def solution():
    """Deborah has four letters to mail. Standard postage is $1.08 per letter, with an additional charge for international mail.
    Deborah is mailing two letters internationally, and she is paying $4.60 to mail four letters.
    How many cents is the additional charge per letter for international shipping?"""
    letters = 4
    international_letters = 2
    standard_postage = 1.08
    total_cost = 4.60
    domestic_letters = letters - international_letters
    cost_of_domestic_shipping = domestic_letters * standard_postage
    additional_charge_per_letter = (total_cost - cost_of_domestic_shipping) / international_letters * 100
    result = additional_charge_per_letter
    return result

print(solution())