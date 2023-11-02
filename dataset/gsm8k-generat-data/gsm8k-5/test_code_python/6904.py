def solution():
    jonny_climbed = 1269  # Jonny climbed 1269 stairs last week
    julia_climbed = (1/3)*jonny_climbed - 7  # Julia climbed 7 less than one-third of what Jonny climbed

    # Calculate the total number of stairs climbed by both Jonny and Julia
    total_climbed = jonny_climbed + julia_climbed
    result = total_climbed
    return result

print(solution())