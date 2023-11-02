def solution():
    # Calculate the total savings from January to July
    savings_jan_to_july = 10 * 7

    # Calculate the total savings from August to November
    savings_aug_to_nov = 15 * 4

    # Calculate the remaining amount needed to reach a total savings of $150
    remaining_savings = 150 - (savings_jan_to_july + savings_aug_to_nov)

    # Calculate how much Roe needs to save in December
    december_savings = remaining_savings / 1

    result = december_savings
    return result

print(solution())