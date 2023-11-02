def solution():
    
    total_dogs = 40
    female_dogs = total_dogs * 0.6
    female_pregnant = female_dogs * (3/4)
    total_puppies = female_pregnant * 10
    tenisha_remains = total_puppies - 130
    result = tenisha_remains
    return result

print(solution())