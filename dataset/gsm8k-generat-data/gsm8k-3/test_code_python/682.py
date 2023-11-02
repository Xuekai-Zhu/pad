def solution():
    """Roe saved $10 per month from January to July and saved $15 per month from August to November. How much should she save in December so she will have a total savings of $150 in the year?"""
    # Define the savings per month for the first 7 months and the next 4 months
    SAVINGS_1 = 10
    SAVINGS_2 = 15

    # Calculate the total savings from January to November
    total_savings = (SAVINGS_1 * 7) + (SAVINGS_2 * 4)

    # Calculate the amount she should save in December
    december_savings = 150 - total_savings

    # Display the amount she should save in December
    result = december_savings
    return result

print(solution())