def solution():
    batches_baked = 4
    cookies_per_batch = 24
    people = 16
    cookies_consumed_per_person = (cookies_per_batch * batches_baked) / people
    result = cookies_consumed_per_person
    return result

print(solution())