def solution():
    num_batches = 4
    num_dozen_per_batch = 2
    cookies_per_dozen = 12
    num_people = 16

    # Calculate the total number of cookies baked
    total_cookies = num_batches * num_dozen_per_batch * cookies_per_dozen

    # Calculate the number of cookies each person consumes
    cookies_per_person = total_cookies / num_people
    result = cookies_per_person
    return result

print(solution())