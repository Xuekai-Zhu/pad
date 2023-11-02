def solution():
    jack_black_musician = True
    jack_black_composer = False
    bear_mccreary_composer = True
    similar_interests = True
    overlapping_skills = False
    if jack_black_musician and not jack_black_composer and bear_mccreary_composer and similar_interests and not overlapping_skills:
        result = "unlikely"
    else:
        result = "likely"
    return result

print(solution())