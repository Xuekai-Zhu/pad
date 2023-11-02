def solution():
    rumi_wrote_poetry = True
    magazine_serializes_longform_prose = True
    if rumi_wrote_poetry and magazine_serializes_longform_prose:
        result = "no"
    else:
        result = "unknown"
    return result

print(solution())