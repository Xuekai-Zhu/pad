def solution():
    """Deborah has four letters to mail. Standard postage is $1.08 per letter, with an additional charge for international mail. Deborah is mailing two letters internationally, and she is paying $4.60 to mail four letters. How many cents is the additional charge per letter for international shipping?"""
    # Define the cost of standard postage and the number of letters
    STANDARD_POSTAGE = 108
    NUM_LETTERS = 4

    # Define the number of international letters and the total cost of mailing
    NUM_INTERNATIONAL = 2
    TOTAL_COST = 460

    # Calculate the cost of mailing the domestic letters
    domestic_cost = (NUM_LETTERS - NUM_INTERNATIONAL) * STANDARD_POSTAGE

    # Calculate the cost of international postage
    international_cost = TOTAL_COST - domestic_cost

    # Calculate the additional cost of international postage per letter
    additional_cost = international_cost / NUM_INTERNATIONAL

    # Convert the additional cost to cents
    additional_cost_cents = int(additional_cost * 100)

    # Return the result
    result = additional_cost_cents
    return result

print(solution())