def solution():
    speed_jenny = 15
    speed_anna = 45
    time_jenny = .5
    time_anna = time_jenny + (time_jenny / speed_anna) * speed_jenny
    result = time_anna * 60
    return result

print(solution())