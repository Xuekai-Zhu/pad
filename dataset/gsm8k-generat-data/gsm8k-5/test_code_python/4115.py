def solution():
    classmates = 24  # Linda has 24 classmates
    cookies_per_student = 10  # Linda wants to give each student 10 cookies
    total_cookies_needed = classmates * cookies_per_student  # Linda needs to make a total of 240 cookies
    cookies_per_batch = 4 * 12  # Each batch of cookies makes 48 cookies

    # Calculate the number of batches of cookies Linda has made
    batches_made = 2 + 1  # Linda made 2 batches of chocolate chip and 1 batch of oatmeal raisin cookies

    # Calculate the number of batches of cookies Linda still needs to make
    batches_needed = (total_cookies_needed - batches_made * cookies_per_batch) / cookies_per_batch

    # Round up to the nearest whole number of batches
    batches_needed = math.ceil(batches_needed)

    result = batches_needed
    return result

print(solution())