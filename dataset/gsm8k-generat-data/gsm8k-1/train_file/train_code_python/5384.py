def solution():
    """The ratio of boys to girls at the dance was 3:4. There were 60 girls at the dance. The teachers were 20% of the number of boys. How many people were at the dance?"""
    girls = 60
    boys_to_girls_ratio = 3/4
    boys = int(girls / boys_to_girls_ratio)
    teachers_percent = 20
    teacher_count = int(boys * (teachers_percent/100))
    total_people = girls + boys + teacher_count
    result = total_people
    
    return result

print(solution())