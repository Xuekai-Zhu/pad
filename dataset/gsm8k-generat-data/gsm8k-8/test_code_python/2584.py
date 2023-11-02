def solution():
    total_flyers = 200
    flyers_passed_out = 42 + 67 + 51
    belinda_flyers = total_flyers - flyers_passed_out

    # Calculate the percentage of flyers Belinda passed out
    belinda_percentage = (belinda_flyers / total_flyers) * 100
    result = belinda_percentage
    return result

print(solution())