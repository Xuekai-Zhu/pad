def solution():
    
    total_students = 100
    girls = total_students // 2
    boys = total_students // 2
    girls_with_dogs = 0.2 * girls
    boys_with_dogs = 0.1 * boys
    total_with_dogs = girls_with_dogs + boys_with_dogs
    result = total_with_dogs
    return result

print(solution())