def solution():
    # Calculate total savings from January to July
    savings_jan_to_july = 10 * 7  # Roe saved $10 per month from January to July

    # Calculate total savings from August to November
    savings_aug_to_nov = 15 * 4  # Roe saved $15 per month from August to November

    # Calculate remaining savings needed in December to reach a total savings of $150
    remaining_savings = 150 - (savings_jan_to_july + savings_aug_to_nov)

    # Calculate how much Roe needs to save in December
    savings_dec = remaining_savings

    result = savings_dec
    return result

print(solution())