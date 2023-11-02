def solution():
    total_aprons = 150  # Heather needs to sew 150 aprons
    aprons_sewn = 13 + 3 * 13  # Heather has already sewn 13 aprons, and today she sewed three times as many
    remaining_aprons = total_aprons - aprons_sewn  # Heather still needs to sew this many aprons
    target_remaining_aprons = remaining_aprons / 2  # Heather wants to sew half of the remaining aprons tomorrow

    # Calculate how many aprons Heather needs to sew tomorrow
    aprons_to_sew_tomorrow = target_remaining_aprons - (3 * 13)

    result = aprons_to_sew_tomorrow
    return result

print(solution())