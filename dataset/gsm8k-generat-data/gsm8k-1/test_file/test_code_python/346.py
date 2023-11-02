def solution():
    """Peyton scheduled after-work activities of a one hour yoga class on Monday, 
    a cooking class that lasts three times as long as Monday’s yoga on Tuesday, a 
    half-hour cheese-tasting event on Wednesday, a museum tour that takes half as 
    long as the cooking class on Thursday, and two hours of errands on Friday. 
    How many hours will all Peyton’s after-work activities take?"""
    monday = 1
    tuesday = 3 * monday
    wednesday = 0.5
    thursday = 0.5 * tuesday
    friday = 2
    total_hours = monday + tuesday + wednesday + thursday + friday
    result = total_hours
    return result

print(solution())