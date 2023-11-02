def solution():
    """Karen is a dog groomer. Rottweilers take 20 minutes to groom, border collies take 10 minutes to groom, and chihuahuas take 45 minutes to groom because they ferociously resist. How many minutes will it take Karen to groom 6 Rottweilers, 9 border collies and 1 chihuahua?"""
    rottweilers = 6
    border_collies = 9
    chihuahuas = 1
    rottweiler_time = 20
    border_collie_time = 10
    chihuahua_time = 45
    total_time = (rottweilers * rottweiler_time) + (border_collies * border_collie_time) + (chihuahuas * chihuahua_time)
    result = total_time
    return result

print(solution())