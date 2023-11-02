def solution():
    """Mark had 10 pieces of fruit to eat in school this week. On Friday, he decided to keep 2 pieces of fruit for next week. He then brings the remaining 3 pieces of fruit to school for the day. How many pieces of fruit did Mark eat in the first four days of the week?"""
    total_fruit = 10
    kept_fruit = 2
    remaining_fruit = total_fruit - kept_fruit
    brought_fruit = 3
    eaten_fruit = remaining_fruit - brought_fruit
    eaten_in_4_days = eaten_fruit // 2 * 4 # assuming Mark eats the same amount each day
    result = eaten_in_4_days
    return result

print(solution())