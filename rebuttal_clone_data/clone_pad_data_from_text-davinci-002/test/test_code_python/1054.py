def solution():
    stitches_per_minute = 4
    stitches_per_flower = 60
    stitches_per_unicorn = 180
    stitches_per_godzilla = 800
    flowers = 50
    unicorns = 3
    godzillas = 1
    total_stitches = (flowers * stitches_per_flower) + (unicorns * stitches_per_unicorn) + (godzillas * stitches_per_godzilla)
    minutes = total_stitches / stitches_per_minute
    result = minutes
    return result

print(solution())