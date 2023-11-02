def solution():
    """Billy ate 20 apples this week. On Monday, he ate 2 apples. On Tuesday, he ate twice as many as he ate the day before. He’s not sure what he ate on Wednesday. On Thursday, he ate four times as many as he ate on Friday. On Friday, he ate half of the amount he ate on Monday. How many apples did he eat on Wednesday?"""
    total_apples = 20
    monday_apples = 2
    friday_apples = monday_apples / 2
    thursday_apples = 4 * friday_apples
    tuesday_apples = 2 * monday_apples
    wednesday_apples = total_apples - monday_apples - tuesday_apples - thursday_apples - friday_apples
    result = wednesday_apples
    return result

print(solution())