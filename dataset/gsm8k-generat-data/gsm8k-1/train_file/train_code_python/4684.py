def solution():
    """Mark had 10 pieces of fruit to eat in school this week. On Friday, he decided to keep 2 pieces of fruit for next week. He then brings the remaining 3 pieces of fruit to school for the day. How many pieces of fruit did Mark eat in the first four days of the week?"""
    total_fruit = 10
    fruit_kept = 2
    fruit_brought_to_school = 3
    fruit_eaten = total_fruit - fruit_kept - fruit_brought_to_school
    result = fruit_eaten
    return result

print(solution())