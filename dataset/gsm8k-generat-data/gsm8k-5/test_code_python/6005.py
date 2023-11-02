def solution():
    stories = 25  # The building has 25 stories
    apartments_per_story = 4  # There are 4 apartments on each floor
    people_per_apartment = 2  # Each apartment houses 2 people

    # Calculate the total number of people in the building
    total_people = stories * apartments_per_story * people_per_apartment

    result = total_people
    return result

print(solution())