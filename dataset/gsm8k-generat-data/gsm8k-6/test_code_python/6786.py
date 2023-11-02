def solution():
    # Calculate how many inches Sandy's nails need to grow
    needed_growth = 26 - 2  # Sandy's nails are currently 2 inches long, and the world record is 26 inches

    # Calculate how many months it will take for her nails to grow that much
    months_needed = needed_growth / (1/10)  # Sandy's nails grow at a rate of one-tenth of an inch per month

    # Calculate how old Sandy will be when she achieves the world record
    age_at_record = round(months_needed / 12) + 12

    result = age_at_record
    return result

print(solution())