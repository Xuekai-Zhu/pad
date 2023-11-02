def solution():
    # Calculate the number of aprons Heather still needs to sew
    remaining_aprons = 150 - 13 - (3 * 13)  # Heather sewed 3 times as many aprons as the initial 13 she had already sewn

    # Calculate the number of aprons Heather should sew tomorrow
    tomorrow_aprons = remaining_aprons / 2

    result = tomorrow_aprons
    return result

print(solution())