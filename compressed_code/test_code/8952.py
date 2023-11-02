def solution():
    
    batches = 4
    dozen = 2
    cookies_per_batch = 12  
    total_cookies = batches * dozen * cookies_per_batch
    people = 16
    cookies_per_person = total_cookies / people
    result = cookies_per_person
    return result

print(solution())