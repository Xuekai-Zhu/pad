def solution():
    # Calculate the total number of cookies baked by Beth
    total_cookies = 4 * 2 * 12  # 4 batches, 2 dozens in each batch

    # Calculate the number of cookies each person consumes
    cookies_per_person = total_cookies / 16

    result = cookies_per_person
    return result

print(solution())