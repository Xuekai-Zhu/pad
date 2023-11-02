def solution():
    """Kevin's fish tank was leaking slowly at a rate of 1.5 ounces per hour. He planned to go to the fish tank store later that day to get a new tank, but it may be as long as 12 hours before he can return home with the new tank. Therefore, to collect the leaking fluid over that time, he placed a bucket underneath the tank that could hold twice the amount of fluid that would leak over 12 hours. What size bucket, in ounces, did he use?"""
    leak_rate = 1.5  # ounces per hour
    time = 12  # hours
    total_leak = leak_rate * time
    bucket_size = total_leak * 2
    result = bucket_size
    return result

print(solution())