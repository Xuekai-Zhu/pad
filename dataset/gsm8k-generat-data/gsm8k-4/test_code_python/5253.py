def solution():
    """Cary starts working at Game Stop for $10/hour. She gets a 20% raise the first year, but the second year the company's profits decrease and her pay is cut to 75% of what it used to be. How much does Cary make now?"""
    # Define Cary's initial pay rate
    pay_rate = 10

    # Calculate Cary's pay after the first year
    pay_rate = pay_rate * 1.2

    # Calculate Cary's pay after the second year
    pay_rate = pay_rate * 0.75

    result = pay_rate
    return result

print(solution())