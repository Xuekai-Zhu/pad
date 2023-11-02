def solution():
    christian_concept = "Holy Spirit"
    hindu_concept = "Krishna"
    christian_description = "an aspect or agent of God that does good in the world"
    hindu_description = "a manifestation of the God Vishnu that brings compassion, tenderness, and love into the world"
    if christian_description == hindu_description:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())