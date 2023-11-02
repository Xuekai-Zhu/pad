def solution():
    num_letters = 4
    postage_per_letter = 1.08
    num_international_letters = 2
    total_cost = 4.60

    # Calculate the cost of standard postage for all letters
    standard_postage_cost = num_letters * postage_per_letter

    # Calculate the additional cost for international shipping
    international_shipping_cost = total_cost - standard_postage_cost

    # Calculate the additional charge per letter for international shipping
    additional_charge_per_letter = international_shipping_cost / num_international_letters * 100
                         # Multiply by 100 to convert to cents
    result = additional_charge_per_letter
    return result

print(solution())