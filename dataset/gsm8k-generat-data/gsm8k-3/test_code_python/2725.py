def solution():
    """Tenisha had 40 dogs that she kept at home as pets. If 60% of them are female, and 3/4 of the female gives birth to 10 puppies each, calculate the total number of puppies that Tenisha remains with after donating 130 puppies to the church."""
    # Calculate the number of female dogs and male dogs
    female_dogs = 0.6 * 40
    male_dogs = 40 - female_dogs

    # Calculate the number of female dogs giving birth to puppies
    female_giving_birth = 0.75 * female_dogs

    # Calculate the total number of puppies
    total_puppies = female_giving_birth * 10

    # Calculate the remaining number of puppies after donating to the church
    remaining_puppies = total_puppies - 130

    # Display the remaining number of puppies
    result = remaining_puppies
    return result

print(solution())