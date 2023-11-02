def solution():
    total_students = 24
    cookies_per_student = 10
    total_cookies_needed = total_students * cookies_per_student

    chocolate_chip_batches = 2
    oatmeal_batches = 1
    cookies_per_batch = 4 * 12

    total_cookies_made = (chocolate_chip_batches + oatmeal_batches) * cookies_per_batch

    remaining_cookies_needed = total_cookies_needed - total_cookies_made
    batches_to_bake = remaining_cookies_needed // cookies_per_batch
    if remaining_cookies_needed % cookies_per_batch != 0:
        batches_to_bake += 1
    result = batches_to_bake
    return result

print(solution())