def solution():
    
    total_purses = 26
    total_handbags = 24
    fake_purses = total_purses / 2
    fake_handbags = total_handbags / 4
    genuine_purses = total_purses - fake_purses
    genuine_handbags = total_handbags - fake_handbags
    total_genuine = genuine_purses + genuine_handbags
    result = total_genuine
    return result

print(solution())