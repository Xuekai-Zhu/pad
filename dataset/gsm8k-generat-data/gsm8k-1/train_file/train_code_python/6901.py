def solution():
    """Misty's favorite number is 3 times smaller than Glory's favorite number. If Glory's favorite number is 450, what's the sum of their favorite numbers?"""
    glory_fav_num = 450
    misty_fav_num = glory_fav_num / 3
    sum_of_fav_nums = glory_fav_num + misty_fav_num
    result = sum_of_fav_nums
    return result

print(solution())