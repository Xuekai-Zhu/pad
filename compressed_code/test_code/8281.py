def solution():
    
    cookies_per_batch = 12
    total_people = 4
    num_batches = 3
    total_cookies = cookies_per_batch * num_batches
    total_chips = total_cookies * 2
    chips_per_person = total_chips / total_people
    result = chips_per_person
    return result

print(solution())