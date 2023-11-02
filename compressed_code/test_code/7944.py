def solution():
    
    num_dogs = 40
    female_dogs = num_dogs * 0.6
    num_puppies = (female_dogs * 0.75) * 10
    remaining_puppies = num_puppies - 130
    result = remaining_puppies
    return result

print(solution())