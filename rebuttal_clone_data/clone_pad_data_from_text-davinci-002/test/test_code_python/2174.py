def solution():
    barry_nice = 1
    kevin_nice = 0.5
    julie_nice = 0.75
    joe_nice = 0.1
    barry_crowd = 24
    kevin_crowd = 20
    julie_crowd = 80
    joe_crowd = 50
    total_nice = (barry_nice * barry_crowd) + (kevin_nice * kevin_crowd) + (julie_nice * julie_crowd) + (joe_nice * joe_crowd)
    result = total_nice
    
    return result

print(solution())