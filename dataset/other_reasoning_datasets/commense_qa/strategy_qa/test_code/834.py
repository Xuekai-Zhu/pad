def solution():
    jpmorgan_assets = 2687000000000
    american_population = 328953020
    amount_per_american = 10
    total_amount_needed = american_population * amount_per_american
    if jpmorgan_assets >= total_amount_needed:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())