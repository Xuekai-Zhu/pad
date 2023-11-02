def solution():
    # Calculate the number of crayons in Beatrice's box
    beatrice_crayons = 128 / 2

    # Calculate the number of crayons in Gilbert's box
    gilbert_crayons = beatrice_crayons / 2

    # Calculate the number of crayons in Judah's box
    judah_crayons = gilbert_crayons / 4

    result = judah_crayons
    return result

print(solution())