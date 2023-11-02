def solution():
    # Define the cost for domestic shipping
    domestic_cost = 1.08

    # Calculate the total cost for all four letters
    total_cost = 4.60

    # Calculate the cost for international shipping
    international_cost = (total_cost - 2 * domestic_cost) / 2

    # Convert the international cost to cents
    international_cost_cents = international_cost * 100

    # Calculate the additional charge per letter for international shipping
    additional_charge = international_cost_cents - domestic_cost * 100

    result = additional_charge
    return result

print(solution())