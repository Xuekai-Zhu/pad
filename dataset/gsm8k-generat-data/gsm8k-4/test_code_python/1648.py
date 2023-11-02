def solution():
    """Kenny wants to make sure he does more jumping jacks every week than he did the week before. He recorded that last week he did 324 total jumping jacks. On Saturday of this week, he looks at his records and sees that on Sunday he did 34. On Monday he did 20. On Tuesday he skipped a day. On Wednesday he did 123. On Thursday he did 64. On Friday he did 23. How many does he have to do on Saturday to make sure he beats last week's number?"""
    # Calculate the total number of jumping jacks done so far this week
    weekly_jj = 34 + 20 + 0 + 123 + 64 + 23

    # Calculate the number of jumping jacks needed to beat last week's total
    needed_jj = 324 - weekly_jj + 1

    result = needed_jj
    return result

print(solution())