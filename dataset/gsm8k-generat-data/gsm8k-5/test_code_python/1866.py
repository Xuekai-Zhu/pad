def solution():
    stitches_per_minute = 4  # Carolyn can sew 4 stitches per minute
    flowers = 50  # Carolyn wants to embroider 50 flowers
    unicorns = 3  # Carolyn wants to embroider 3 unicorns
    godzilla = 1  # Carolyn wants to embroider 1 Godzilla

    # Calculate the total number of stitches Carolyn needs to embroider
    total_stitches = (flowers * 60) + (unicorns * 180) + (godzilla * 800)

    # Calculate the total time Carolyn needs to spend embroidering
    total_time = total_stitches / stitches_per_minute
    result = total_time
    return result

print(solution())