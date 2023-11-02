def solution():
    """There were 80 people at a football game on Saturday. On Monday, 20 fewer people were at the football game.
    On Wednesday, 50 more people were at the game than on Monday. On Friday, there were the same number of people
    as on Saturday and Monday combined. If their expected total audience at the football game for a week is 350,
    how many more people attended the games than they had expected?"""
    saturday = 80
    monday = saturday - 20
    wednesday = monday + 50
    friday = saturday + monday
    total_audience = saturday + monday + wednesday + friday
    expected_audience = 350
    extra_audience = total_audience - expected_audience
    result = extra_audience
    return result

print(solution())