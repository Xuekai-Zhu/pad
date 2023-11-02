def solution():
    """There are some kids in camp. Half of the kids are going to soccer camp, and 1/4 of the kids going to soccer camp are going to soccer camp in the morning. 750 kids are going to soccer camp in the afternoon. How many kids there in camp altogether?"""
    kids_in_soccer_camp_afternoon = 750
    percent_in_soccer_camp_morning = 0.25
    total_percent_in_soccer_camp = 0.5
    kids_in_soccer_camp_morning = kids_in_soccer_camp_afternoon * percent_in_soccer_camp_morning / total_percent_in_soccer_camp
    total_kids_in_camp = 2 * (kids_in_soccer_camp_afternoon + kids_in_soccer_camp_morning)
    result = total_kids_in_camp
    return result

print(solution())