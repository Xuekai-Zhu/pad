def solution():
    glass_resonant_freq = "middle C"
    kelly_clarkson_vocal_range = "three octaves"
    song_key = "A-flat"
    above_middle_C = True
    if above_middle_C and kelly_clarkson_vocal_range >= "middle C":
        result = "yes"
    else:
        result = "no"
    return result

print(solution())