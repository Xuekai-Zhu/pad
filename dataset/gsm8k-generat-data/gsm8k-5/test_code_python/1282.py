def solution():
    karen_crayons = 128  # Karen's box had 128 crayons
    beatrice_crayons = karen_crayons / 2  # Beatrice's box had half as many crayons as Karen's
    gilbert_crayons = beatrice_crayons * 2  # Gilbert's box had twice as many crayons as Beatrice's
    judah_crayons = gilbert_crayons / 4  # Judah's box had four times fewer crayons than Gilbert's
    result = judah_crayons
    return result

print(solution())