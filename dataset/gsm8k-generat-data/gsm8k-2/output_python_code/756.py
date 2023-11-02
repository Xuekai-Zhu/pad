def solution():
    """Luna, the poodle, is supposed to eat 2 cups of kibble every day. But Luna's master, Mary, and her husband, Frank, sometimes feed Luna too much kibble. One day, starting with a new, 12-cup bag of kibble, Mary gave Luna 1 cup of kibble in the morning and 1 cup of kibble in the evening, But on the same day, Frank also gave Luna 1 cup of kibble in the afternoon and twice as much in the late evening as he had given Luna in the afternoon. The next morning, how many cups of kibble will Mary find remaining in the bag?"""
    bag_size = 12
    mary_day_total = 2
    mary_total = mary_day_total * 2
    frank_afternoon = 1
    frank_late_evening = frank_afternoon * 2
    total_given = mary_day_total + mary_day_total + frank_afternoon + frank_late_evening
    remaining_kibble = bag_size - total_given
    result = remaining_kibble
    return result

print(solution())