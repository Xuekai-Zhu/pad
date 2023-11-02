def solution():
    """Ellie takes her little brother down to the pond to teach him how to skip stones. After he takes his first throw, she gives him pointers to improve his technique. His second throw skips two more times across the water than his first. His third throw skips twice as many times as his second. His fourth throw skips 3 fewer times than his third throw. His fifth throw skips one more time than the fourth throw. If his fifth throw skipped 8 times across the water, how many skips did he make in total between all of his throws?"""
    first_throw = 1
    second_throw = first_throw + 2
    third_throw = second_throw * 2
    fourth_throw = third_throw - 3
    fifth_throw = fourth_throw + 1
    
    total_skips = first_throw + second_throw + third_throw + fourth_throw + fifth_throw
    
    result = total_skips
    return result

print(solution())