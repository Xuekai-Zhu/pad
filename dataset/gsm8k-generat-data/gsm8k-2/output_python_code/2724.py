def solution():
    """Tenisha had 40 dogs that she kept at home as pets. If 60% of them are female, and 3/4 of the female gives birth to 10 puppies each, calculate the total number of puppies that Tenisha remains with after donating 130 puppies to the church."""
    total_dogs = 40
    female_dogs = total_dogs * 0.6
    female_pregnant = female_dogs * (3/4)
    total_puppies = female_pregnant * 10
    tenisha_remains = total_puppies - 130
    result = tenisha_remains
    return result

print(solution())