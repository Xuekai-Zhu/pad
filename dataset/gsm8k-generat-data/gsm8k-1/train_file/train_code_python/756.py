def solution():
    """Luna, the poodle, is supposed to eat 2 cups of kibble every day. But Luna's master, Mary, and her husband, Frank, sometimes feed Luna too much kibble. One day, starting with a new, 12-cup bag of kibble, Mary gave Luna 1 cup of kibble in the morning and 1 cup of kibble in the evening, But on the same day, Frank also gave Luna 1 cup of kibble in the afternoon and twice as much in the late evening as he had given Luna in the afternoon. The next morning, how many cups of kibble will Mary find remaining in the bag?"""
    total_kibble = 12
    kibble_eaten = 1 + 1 + 1 + 2
    kibble_remaining = total_kibble - kibble_eaten
    result = kibble_remaining
    return result

print(solution())