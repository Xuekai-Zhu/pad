def solution():
    
    total_balls = 100
    defective_balls = int(total_balls * 0.4)
    useable_balls = total_balls - defective_balls
    exploded_balls = int(useable_balls * 0.2)
    inflated_balls = useable_balls - exploded_balls
    result = inflated_balls
    return result

print(solution())