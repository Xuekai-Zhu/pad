def solution():
    """Billy ate 20 apples this week. On Monday, he ate 2 apples. On Tuesday, he ate twice as many as he ate the day before. He’s not sure what he ate on Wednesday. On Thursday, he ate four times as many as he ate on Friday. On Friday, he ate half of the amount he ate on Monday. How many apples did he eat on Wednesday?"""
    monday = 2
    tuesday = monday * 2
    friday = monday / 2
    thursday = friday * 4
    total = monday + tuesday + friday + thursday
    wednesday = 20 - total
    result = wednesday
    return result

print(solution())