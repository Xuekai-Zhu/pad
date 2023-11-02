def solution():
    total_letters = 4  # Deborah is mailing four letters in total
    international_letters = 2  # Two of the letters are being sent internationally
    domestic_letters = total_letters - international_letters  # The remaining letters are being sent domestically
    total_cost = 460  # Deborah is paying $4.60 to mail four letters

    # Calculate the cost of sending the domestic letters
    domestic_cost = domestic_letters * 108  # Standard postage is $1.08 per letter

    # Calculate the additional cost per international letter
    international_cost = (total_cost - domestic_cost) / international_letters
    additional_cost = (international_cost - 108) * 100  # Convert to cents

    result = additional_cost
    return result

print(solution())