def solution():
    """A special balloon increases by two-fifths of its previous volume every hour when placed under water. If its original volume is 500cm³, what will its volume be after 2 hours underwater?"""
    original_volume = 500
    increase_percent = 2/5
    time_underwater = 2
    total_increase = ((1 + increase_percent)**time_underwater) - 1
    new_volume = original_volume * (1 + total_increase)
    result = new_volume
    return result

print(solution())