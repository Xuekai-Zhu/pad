def solution():
    """Suzanne wants to raise money for charity by running a 5-kilometer race. Her parents have pledged to donate $10 for her first kilometer and double the donation for every successive kilometer. If Suzanne finishes the race, how much money will her parents donate?"""
    km1 = 10
    km2 = km1 * 2
    km3 = km2 * 2
    km4 = km3 * 2
    km5 = km4 * 2
    total_donation = km1 + km2 + km3 + km4 + km5
    result = total_donation
    return result

print(solution())