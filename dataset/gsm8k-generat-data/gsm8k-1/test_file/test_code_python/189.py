def solution():
    """Sue lives in a fun neighborhood. One weekend, the neighbors decided to play a prank on Sue. On Friday morning, the neighbors placed 18 pink plastic flamingos out on Sue's front yard. On Saturday morning, the neighbors took back one third of the flamingos, painted them white, and put these newly painted white flamingos back out on Sue's front yard. Then, on Sunday morning, they added another 18 pink plastic flamingos to the collection. At noon on Sunday, how many more pink plastic flamingos were out than white plastic flamingos?"""
    pink_friday = 18
    white_saturday = pink_friday / 3
    pink_sunday = 18
    white_sunday = white_saturday
    pink_total = pink_friday + pink_sunday
    white_total = white_saturday + white_sunday
    difference = pink_total - white_total
    result = difference
    return result

print(solution())