def solution():
    # Calculate Christine's total commission earned
    commission = 0.12 * 24000

    # Calculate the amount she will allocate to her personal needs
    personal_needs = 0.6 * commission

    # Calculate the amount she will save
    savings = commission - personal_needs

    result = savings
    return result

print(solution())