def solution():
    # Calculate the total number of stitches needed to embroider all designs
    total_stitches = (3*180) + (50*60) + 800  # embroidering 3 unicorns, 50 flowers, and Godzilla

    # Calculate the total time needed to embroider all designs
    embroidery_time = total_stitches / 4  # Carolyn can sew 4 stitches/minute
    result = embroidery_time
    return result

print(solution())