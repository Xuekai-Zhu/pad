def solution():
    """Kenny wants to make sure he does more jumping jacks every week than he did the week before. He recorded that last week he did 324 total jumping jacks. On Saturday of this week, he looks at his records and sees that on Sunday he did 34. On Monday he did 20. On Tuesday he skipped a day. On Wednesday he did 123. On Thursday he did 64. On Friday he did 23. How many does he have to do on Saturday to make sure he beats last week's number?"""
    
    # Calculate last week's total jumping jacks
    last_week_total = 324
    
    # Calculate this week's total jumping jacks (excluding Tuesday)
    this_week_total = 34 + 20 + 123 + 64 + 23
    
    # Calculate the minimum number of jumping jacks Kenny needs to do on Saturday to beat last week's number
    min_jump_jacks = last_week_total - this_week_total + 1
    
    result = min_jump_jacks
    return result

print(solution())