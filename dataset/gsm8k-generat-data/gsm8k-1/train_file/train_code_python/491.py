def solution():
    """There are 40 Judges in the state of Rhode Island. 10 percent of Judges are under 30 years old. 60 percent of Judges are 30-50 years old. The rest of the Judges are over 50 years old. How many Judges are over 50 years old?"""
    total_judges = 40
    under_thirty_percent = 0.1
    thirty_to_fifty_percent = 0.6
    under_thirty = total_judges * under_thirty_percent
    thirty_to_fifty = total_judges * thirty_to_fifty_percent
    over_fifty = total_judges - under_thirty - thirty_to_fifty
    result = over_fifty
    return result

print(solution())