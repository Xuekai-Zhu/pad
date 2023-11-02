def solution():
    pat_stick = 30
    dirt_covered = 7

    # Calculate the length of the uncovered portion of Pat's stick
    pat_uncovered = pat_stick - dirt_covered

    # Calculate the length of Sarah's stick
    sarah_stick = pat_uncovered * 2

    # Calculate the length of Jane's stick in inches
    jane_stick = (sarah_stick / 12) - 2

    # Convert length of Jane's stick to inches
    jane_stick_inches = jane_stick * 12
    result = jane_stick_inches
    return result

print(solution())