def solution():
    
    classmates = 24
    cookies_per_student = 10
    total_cookies_needed = classmates * cookies_per_student
    cookies_per_recipe = 4 * 12
    chocolate_chip_batches = 2
    oatmeal_raisin_batches = 1
    cookies_made = (chocolate_chip_batches + oatmeal_raisin_batches) * cookies_per_recipe
    cookies_left_to_make = total_cookies_needed - cookies_made
    batches_left_to_make = cookies_left_to_make // cookies_per_recipe
    result = batches_left_to_make
    return result

print(solution())