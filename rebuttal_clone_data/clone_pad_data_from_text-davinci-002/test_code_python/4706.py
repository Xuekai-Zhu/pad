def solution():
     bag_size = 81
     chips_per_cookie = 9
     chips_used = bag_size / 3
     cookies_per_batch = chips_used / chips_per_cookie
     result = cookies_per_batch
 
    return result

print(solution())