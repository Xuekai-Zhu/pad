def solution():
    """Jim starts with $80 in his investment portfolio. After 1 year it grows by 15%. He then adds another $28 to his portfolio. After 1 more year the combined portfolio grows by 10%. What is his final portfolio worth after 2 years from when he started?"""
    starting_portfolio = 80
    first_year_growth = 0.15
    first_year_ending_portfolio = starting_portfolio * (1 + first_year_growth)
    second_year_contribution = 28
    second_year_growth = 0.1
    final_portfolio = (first_year_ending_portfolio + second_year_contribution) * (1 + second_year_growth)
    result = final_portfolio
    return result

print(solution())