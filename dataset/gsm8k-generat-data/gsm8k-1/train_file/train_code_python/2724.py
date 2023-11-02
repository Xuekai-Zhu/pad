def solution():
    """Tenisha had 40 dogs that she kept at home as pets. If 60% of them are female, and 3/4 of the female gives birth to 10 puppies each, calculate the total number of puppies that Tenisha remains with after donating 130 puppies to the church."""
    num_dogs = 40
    female_dogs = num_dogs * 0.6
    num_puppies = (female_dogs * 0.75) * 10
    remaining_puppies = num_puppies - 130
    result = remaining_puppies
    return result

print(solution())