def solution():
    # Define the number of stitches for each design
    flower_stitches = 60
    unicorn_stitches = 180
    godzilla_stitches = 800

    # Calculate the total number of stitches
    total_stitches = (3 * unicorn_stitches) + (50 * flower_stitches) + godzilla_stitches

    # Calculate the time required to embroider all designs
    time_required = total_stitches / 4

    result = time_required
    return result

print(solution())