def solution():
    """Cary starts working at Game Stop for $10/hour. She gets a 20% raise the first year, but the second year the company's profits decrease and her pay is cut to 75% of what it used to be. How much does Cary make now?"""
    starting_pay = 10
    first_year_raise = 0.2
    second_year_cut = 0.25
    first_year_pay = starting_pay * (1 + first_year_raise)
    second_year_pay = first_year_pay * (1 - second_year_cut)
    result = second_year_pay
    return result

print(solution())