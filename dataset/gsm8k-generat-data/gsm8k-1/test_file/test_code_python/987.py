def solution():
    """Comet Halley orbits the sun every 75 years. Bill's dad saw the Comet when he was 30 years old. Bill saw the comet a second time when he was three times the age his father was when he saw the Comet. How old was Bill when he saw the Comet for the first time?"""
    comet_period = 75
    dad_age_at_first_sighting = 30
    bill_age_at_second_sighting = dad_age_at_first_sighting * 3
    years_between_sightings = bill_age_at_second_sighting - dad_age_at_first_sighting
    bill_age_at_first_sighting = dad_age_at_first_sighting - years_between_sightings
    result = bill_age_at_first_sighting
    return result

print(solution())