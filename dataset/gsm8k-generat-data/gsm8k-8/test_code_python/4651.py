def solution():
    # Define the total number of aprons needed
    total_aprons_needed = 150

    # Define the number of aprons Heather has already sewed
    aprons_sewed = 13

    # Calculate the number of aprons Heather sewed today
    aprons_sewed_today = 3 * aprons_sewed

    # Calculate the remaining number of aprons needed
    remaining_aprons_needed = total_aprons_needed - aprons_sewed - aprons_sewed_today

    # Calculate the number of aprons Heather should sew tomorrow
    aprons_sew_tomorrow = remaining_aprons_needed / 2

    result = aprons_sew_tomorrow
    return result

print(solution())