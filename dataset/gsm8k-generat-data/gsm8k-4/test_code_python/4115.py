def solution():
    """Linda was going to pass out homemade cookies to each of her 24 classmates on the last day of school. She wanted to give each student 10 cookies and wanted to make chocolate chip cookies and oatmeal raisin cookies. Each cookie recipe made exactly 4 dozen cookies. She was able to make 2 batches of chocolate chip cookies before running out of chocolate chips. She made 1 batch of oatmeal raisin cookies. How many more batches of cookies does Linda need to bake?"""
    # Define the number of students and the number of cookies each student should receive
    num_students = 24
    cookies_per_student = 10

    # Calculate the total number of cookies needed
    total_cookies_needed = num_students * cookies_per_student

    # Define the number of cookies per batch
    cookies_per_batch = 4 * 12

    # Calculate the number of chocolate chip cookies Linda made
    cc_cookies = 2 * cookies_per_batch

    # Calculate the number of oatmeal raisin cookies Linda made
    or_cookies = 1 * cookies_per_batch

    # Calculate the total number of cookies Linda made
    total_cookies_made = cc_cookies + or_cookies

    # Calculate the number of batches Linda still needs to make
    batches_needed = (total_cookies_needed - total_cookies_made) / cookies_per_batch

    # Round up to the nearest whole number of batches
    batches_needed = math.ceil(batches_needed)

    result = batches_needed
    return result

print(solution())