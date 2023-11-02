def solution():
    """A teacher uses a 5-inch piece of chalk to write math equations on a chalkboard for his students. The teacher likes to conserve chalk, so he tries to only use 20% of the chalk each day. Since the teacher cannot write with a very small piece of chalk, he recycles the chalk when it is smaller than 2 inches. On Monday the teacher used a new piece of chalk. His students need extra help that day, so he ended up writing more than usual. He used up 45% of the chalk by the end of the day. If the teacher goes back to using only 20% of the chalk each day, how many days does he have before he has to recycle this piece?"""
    total_chalk = 5
    used_chalk_on_monday = 0.45 * total_chalk
    remaining_chalk = total_chalk - used_chalk_on_monday
    
    # Determine how many days the remaining chalk will last
    days = 0
    while remaining_chalk >= 2:
        used_chalk = 0.2 * remaining_chalk
        remaining_chalk -= used_chalk
        days += 1
    
    result = days
    return result

print(solution())