def solution():
    # Calculate the cost of mailing two letters domestically and two letters internationally
    domestic_cost = 1.08 * 2
    international_cost = 1.08 * 2 + additional_charge  # additional charge is in cents/letter
    total_cost = domestic_cost + international_cost

    # Solve for the additional charge per letter for international shipping
    additional_charge = (4.60 - domestic_cost) / 2  # total cost minus domestic cost divided by number of international letters
    result = additional_charge
    return result

print(solution())