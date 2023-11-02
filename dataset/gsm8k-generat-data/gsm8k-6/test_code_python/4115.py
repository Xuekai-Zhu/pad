def solution():
    # Calculate the total number of cookies Linda has made so far
    cookies_per_recipe = 4 * 12  # each recipe makes 4 dozen (48) cookies
    total_cookies = (2 * cookies_per_recipe) + cookies_per_recipe  # 2 batches of chocolate chip, 1 batch of oatmeal raisin
    cookies_needed = 24 * 10  # Linda wants to give each of her 24 classmates 10 cookies
    batches_needed = (cookies_needed - total_cookies) // cookies_per_recipe + 1  # calculate the number of additional batches needed
    result = batches_needed
    return result

print(solution())