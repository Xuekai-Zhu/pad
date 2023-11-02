def solution():
    triple_crown_races = ["Preakness", "Kentucky Derby", "Belmont Stakes"]
    eid_al_fitr_days = 3
    # Determine the number of days between the first and last Triple Crown race
    days_between_races = (triple_crown_races.index("Belmont Stakes") - 
                          triple_crown_races.index("Preakness")) * 7
    # Check if the number of days between the races is less than or equal to the number of Eid al-Fitr days
    if days_between_races <= eid_al_fitr_days:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())