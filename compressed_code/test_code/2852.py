def solution():
    
    total_purses = 26
    total_handbags = 24
    fake_purses = total_purses / 2
    fake_handbags = total_handbags / 4
    authentic_purses = total_purses - fake_purses
    authentic_handbags = total_handbags - fake_handbags
    total_authentic = authentic_purses + authentic_handbags
    result = total_authentic
    return result

print(solution())