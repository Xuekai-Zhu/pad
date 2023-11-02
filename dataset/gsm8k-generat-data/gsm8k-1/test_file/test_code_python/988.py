def solution():
    """Buford writes many checks every year. Once per month he writes a check to pay the electric bill. He also writes a check every month for the gas bill. Twice per month he writes a check to the church. And quarterly, he writes a check to the pest and lawn service. How many checks does Buford write per year?"""
    checks_per_electricity = 12
    checks_per_gas = 12
    checks_per_church = 2 * 12
    checks_per_pest_lawn = 4
    total_checks = checks_per_electricity + checks_per_gas + checks_per_church + checks_per_pest_lawn
    result = total_checks
    return result

print(solution())