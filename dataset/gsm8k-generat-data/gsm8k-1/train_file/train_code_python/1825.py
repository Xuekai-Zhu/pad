def solution():
    """Miriam is trying to exercise more and figures if she counts her exercises it will be encouraging to see her numbers go up. On Monday she does 5 push-ups. On Tuesday she does 7 push-ups. On Wednesday she does twice as many push-ups as the day before. On Thursday she does half the number of total pushups she already did that week. Finally, on Friday she does as many pushups as the total number she did over the previous four days. How many pushups does Miriam do on Friday?"""
    monday = 5
    tuesday = 7
    wednesday = tuesday * 2
    total_pushups = monday + tuesday + wednesday
    thursday = total_pushups / 2
    friday = total_pushups + monday + tuesday + wednesday + thursday
    result = friday
    return result

print(solution())