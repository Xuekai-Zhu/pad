def solution():
    casey_time = 6  # time taken by Casey to complete the marathon in hours
    zendaya_time = (4/3) * casey_time  # time taken by Zendaya to complete the marathon in hours (1/3 longer than Casey)
    avg_time = (casey_time + zendaya_time) / 2  # average time taken by Casey and Zendaya
    result = avg_time
    return result

print(solution())