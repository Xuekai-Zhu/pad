def solution():
    # Define the dates of the Spanish-American War and the presidency of William McKinley
    war_start_date = "April 21, 1898"
    war_end_date = "August 13, 1898"
    mckinley_presidency_start_date = "March 4, 1897"
    mckinley_presidency_end_date = "September 14, 1901"
    # Check if McKinley died from gun related injuries
    if mckinley_presidency_start_date <= war_start_date and mckinley_presidency_end_date >= war_end_date:
        cause_of_death = "gun related injuries"
        if cause_of_death == "gun related injuries":
            result = "yes"
        else:
            result = "no"
    else:
        result = "no"
    return result

print(solution())