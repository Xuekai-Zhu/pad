def solution():
    # Calculate the total number of items Natalia needs to store
    total_items = 145 + 271 + 419 + 209

    # Calculate the number of crates needed to store the items
    crates_needed = total_items // 9

    # Add an extra crate if there are any remaining items
    if total_items % 9 != 0:
        crates_needed += 1

    result = crates_needed
    return result

print(solution())