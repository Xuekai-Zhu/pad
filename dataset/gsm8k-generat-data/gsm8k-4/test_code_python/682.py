def solution():
    """Roe saved $10 per month from January to July and saved $15 per month from August to November. How much should she save in December so she will have a total savings of $150 in the year?"""
    # Define the savings for each month
    jan_to_july_savings = 10 * 7
    aug_to_nov_savings = 15 * 4

    # Calculate the remaining savings needed for the year
    remaining_savings = 150 - jan_to_july_savings - aug_to_nov_savings

    # Calculate the savings needed for December
    dec_savings = remaining_savings / 1

    result = dec_savings
    return result

print(solution())