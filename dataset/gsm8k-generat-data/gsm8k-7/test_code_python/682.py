def solution():
    # Calculate the total savings from January to July
    savings1 = 10 * 7

    # Calculate the total savings from August to November
    savings2 = 15 * 4

    # Calculate the remaining savings needed to reach the total savings of $150
    remaining_savings = 150 - (savings1 + savings2)

    # Calculate how much to save in December
    savings3 = remaining_savings / 1

    result = savings3
    return result

print(solution())