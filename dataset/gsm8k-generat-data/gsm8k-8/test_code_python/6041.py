def solution():
    # Calculate the total number of items
    total_items = 145 + 271 + 419 + 209

    # Calculate the number of crates needed
    crates_needed = total_items // 9
    if total_items % 9 != 0:
        crates_needed += 1

    result = crates_needed
    return result

print(solution())