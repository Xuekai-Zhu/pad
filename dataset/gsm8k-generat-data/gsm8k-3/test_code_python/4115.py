def solution():
    """Linda was going to pass out homemade cookies to each of her 24 classmates on the last day of school.  She wanted to give each student 10 cookies and wanted to make chocolate chip cookies and oatmeal raisin cookies.  Each cookie recipe made exactly 4 dozen cookies.  She was able to make 2 batches of chocolate chip cookies before running out of chocolate chips.  She made 1 batch of oatmeal raisin cookies.  How many more batches of cookies does Linda need to bake?"""
    # Define the number of students and cookies per student
    num_students = 24
    cookies_per_student = 10

    # Define the number of cookies per batch
    cookies_per_batch = 4 * 12

    # Calculate the total number of cookies needed
    total_cookies_needed = num_students * cookies_per_student

    # Calculate the number of cookies already baked
    cookies_baked = (2 * cookies_per_batch) + cookies_per_batch

    # Calculate the number of batches still needed
    batches_needed = (total_cookies_needed - cookies_baked) // cookies_per_batch

    # Display the number of batches still needed
    result = batches_needed
    return result

print(solution())