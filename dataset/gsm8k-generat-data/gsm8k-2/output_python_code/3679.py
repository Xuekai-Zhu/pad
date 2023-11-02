def solution():
    """Tirzah has a lot of purses and handbags; in total she has 26 purses and 24 handbags. Half the purses and 1/4 the handbags are fake. If the rest are authentic, how many purses and handbags in total are genuine?"""
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