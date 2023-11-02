def solution():
    
    stitches_per_minute = 4
    flower_stitches = 60
    unicorn_stitches = 180
    godzilla_stitches = 800
    total_stitches = (godzilla_stitches + (3*unicorn_stitches) + (50*flower_stitches))
    time_required = total_stitches / stitches_per_minute
    result = time_required
    return result

print(solution())