def solution():
    """Linda was going to pass out homemade cookies to each of her 24 classmates on the last day of school. She wanted to give each student 10 cookies and wanted to make chocolate chip cookies and oatmeal raisin cookies. Each cookie recipe made exactly 4 dozen cookies. She was able to make 2 batches of chocolate chip cookies before running out of chocolate chips. She made 1 batch of oatmeal raisin cookies. How many more batches of cookies does Linda need to bake?"""
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