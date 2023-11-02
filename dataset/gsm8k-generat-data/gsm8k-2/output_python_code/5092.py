def solution():
    """Maurice had only been horseback riding a handful of times in his life. His best friend, Matt, goes horseback riding regularly. When Maurice went to visit Matt for two weeks, he rode another 8 times. Each time, Matt went with him. Meanwhile, besides the times that Matt accompanied Maurice, he rode an additional 16 times. If the total number of times Matt rode during that two weeks is three times the number of times Maurice had ridden before his visit, how many times had Maurice been horseback riding before visiting Matt?"""
    total_rides_with_matt = 8
    total_rides_without_matt = 16
    total_rides_with_maurice = total_rides_with_matt + total_rides_without_matt
    total_rides_for_matt = 3 * total_rides_with_maurice
    rides_before_visit = total_rides_for_matt - total_rides_with_maurice
    result = rides_before_visit
    return result

print(solution())