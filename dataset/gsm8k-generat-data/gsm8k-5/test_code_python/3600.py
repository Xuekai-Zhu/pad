def solution():
    pat_stick = 30  # Pat's stick is 30 inches long
    dirty_portion = 7  # Pat covers 7 inches of his stick with dirt
    clean_portion = pat_stick - dirty_portion  # Calculate the portion of Pat's stick that is not covered in dirt

    # Calculate the length of Sarah's stick, which is twice as long as the clean portion of Pat's stick
    sarah_stick = clean_portion * 2

    # Calculate the length of Jane's stick, which is two feet (24 inches) shorter than Sarah's stick
    jane_stick = sarah_stick - 24
    result = jane_stick
    return result

print(solution())