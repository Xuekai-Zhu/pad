def solution():
    """Kyle can lift 60 more pounds this year, which is 3 times as much as he could lift last year. How many pounds can Kyle lift in all?"""
    weight_increase = 60
    last_year_lift = weight_increase / 3
    total_lift = last_year_lift + weight_increase
    result = total_lift
    return result

print(solution())