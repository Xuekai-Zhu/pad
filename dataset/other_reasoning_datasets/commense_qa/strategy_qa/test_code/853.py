def solution():
    astronomers_study_science_of_stars = True
    horoscopes_written_by_astrologers = True
    if astronomers_study_science_of_stars and not horoscopes_written_by_astrologers:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())