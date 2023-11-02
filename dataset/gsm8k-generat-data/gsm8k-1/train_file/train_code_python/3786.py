def solution():
    """Jason joined the military when he turned 18. It took him 8 years to raise to the rank of chief. Then 25% longer than that to go from chief to master chief. He then spent 10 years more in the military before retiring. How old was he when he retired?"""
    years_to_chief = 8
    years_to_master_chief = years_to_chief + (0.25 * years_to_chief)
    years_until_retirement = years_to_master_chief + 10
    retirement_age = 18 + years_until_retirement
    result = retirement_age
    return result

print(solution())