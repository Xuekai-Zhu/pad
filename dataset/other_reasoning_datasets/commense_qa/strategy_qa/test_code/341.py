def solution():
    haiku_syllables = [5, 7, 5]
    microbes_syllables = [3]
    total_haiku_syllables = sum(haiku_syllables)
    total_microbes_syllables = sum(microbes_syllables)
    if total_microbes_syllables < total_haiku_syllables:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())