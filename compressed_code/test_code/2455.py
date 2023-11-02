def solution():
    
    cookies_per_batch = 12
    total_people = 4
    total_batches = 3
    total_cookies = cookies_per_batch * total_batches
    total_chocolate_chips = total_cookies * 2
    chips_per_person = total_chocolate_chips // total_people
    result = chips_per_person
    return result

print(solution())