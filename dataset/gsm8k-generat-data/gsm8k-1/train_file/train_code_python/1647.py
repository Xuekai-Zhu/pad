def solution():
    """Kenny wants to make sure he does more jumping jacks every week than he did the week before. He recorded that last week he did 324 total jumping jacks. On Saturday of this week, he looks at his records and sees that on Sunday he did 34. On Monday he did 20. On Tuesday he skipped a day. On Wednesday he did 123. On Thursday he did 64. On Friday he did 23. How many does he have to do on Saturday to make sure he beats last week's number?"""
    last_week_total = 324
    current_week_total = sum([34, 20, 0, 123, 64, 23])
    difference = last_week_total - current_week_total
    result = difference + 1  # add 1 to beat last week's number
    return result

print(solution())