def solution():
    
    classmates = 24
    cookies_per_student = 10
    total_cookies_needed = classmates * cookies_per_student
    cookies_per_recipe = 4 * 12
    chocolate_chip_batches = 2
    oatmeal_batches = 1
    total_cookies_made = (chocolate_chip_batches + oatmeal_batches) * cookies_per_recipe
    remaining_cookies_needed = total_cookies_needed - total_cookies_made
    batches_needed = remaining_cookies_needed / cookies_per_recipe
    result = batches_needed
    return result

print(solution())