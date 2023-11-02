def solution():
    # Calculate the total number of cookies baked in a week
    cookies_per_batch = 12 * 2 # 2 dozen cookies per batch
    total_cookies = cookies_per_batch * 4

    # Calculate the number of cookies each person consumes
    num_people = 16
    cookies_per_person = total_cookies / num_people
    result = cookies_per_person
    return result

print(solution())