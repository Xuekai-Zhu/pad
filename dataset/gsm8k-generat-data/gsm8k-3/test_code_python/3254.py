def solution():
    """Deborah has four letters to mail. Standard postage is $1.08 per letter, with an additional charge for international mail. Deborah is mailing two letters internationally, and she is paying $4.60 to mail four letters. How many cents is the additional charge per letter for international shipping?"""
    # Define the cost of standard postage per letter
    POSTAGE_PER_LETTER = 1.08

    # Define the number of international letters
    int_letters = 2

    # Define the total cost to mail all four letters
    total_cost = 4.60

    # Calculate the cost of the two domestic letters
    domestic_cost = (4 - int_letters) * POSTAGE_PER_LETTER

    # Calculate the cost of the two international letters
    international_cost = total_cost - domestic_cost

    # Calculate the additional charge per letter for international shipping in cents
    additional_charge = round((international_cost / int_letters - POSTAGE_PER_LETTER) * 100)

    # Display the additional charge per letter
    result = additional_charge
    return result

print(solution())