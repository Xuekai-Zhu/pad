def solution():
    """A special balloon increases by two-fifths of its previous volume every hour when placed under water. If its original volume is 500cm³, what will its volume be after 2 hours underwater?"""
    original_volume = 500
    increase_factor = 2/5
    volume_after_1_hour = original_volume * (1 + increase_factor)
    volume_after_2_hours = volume_after_1_hour * (1 + increase_factor)
    result = volume_after_2_hours
    return result

print(solution())