def solution():
    stitches_per_minute = 4
    flower_stitches = 60
    unicorn_stitches = 180
    godzilla_stitches = 800

    num_flowers = 50
    num_unicorns = 3

    # Calculate the total number of stitches needed for all flowers
    total_flower_stitches = flower_stitches * num_flowers

    # Calculate the total number of stitches needed for all unicorns
    total_unicorn_stitches = unicorn_stitches * num_unicorns

    # Calculate the total number of stitches needed for Godzilla
    total_godzilla_stitches = godzilla_stitches

    # Calculate the total number of stitches needed for all embroidery
    total_stitches = total_flower_stitches + total_unicorn_stitches + total_godzilla_stitches

    # Calculate the total time needed to embroider everything
    total_time = total_stitches / stitches_per_minute
    result = total_time
    return result

print(solution())