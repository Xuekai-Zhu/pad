def solution():
    # Calculate how much Thomas saved in 6 years
    thomas_savings = 40 * 12 * 6  # $40 per month, 12 months per year, 6 years

    # Calculate how much Joseph saved in 6 years (2/5 times less than Thomas)
    joseph_savings = (3/5) * 40 * 12 * 6  # 3/5 of $40 per month, 12 months per year, 6 years

    # Calculate the total savings of both Thomas and Joseph
    total_savings = thomas_savings + joseph_savings
    result = total_savings
    return result

print(solution())