def solution():
    """It takes 2.5 hours to groom a dog and 0.5 hours to groom a cat. What is the number of minutes it takes to groom 5 dogs and 3 cats?"""
    # Define the time to groom a dog and a cat
    dog_groom_time = 2.5
    cat_groom_time = 0.5

    # Calculate the total grooming time for 5 dogs
    total_dog_groom_time = dog_groom_time * 5

    # Calculate the total grooming time for 3 cats
    total_cat_groom_time = cat_groom_time * 3

    # Calculate the total grooming time in hours
    total_groom_time_hours = total_dog_groom_time + total_cat_groom_time

    # Convert the total grooming time to minutes
    total_groom_time_minutes = total_groom_time_hours * 60

    result = total_groom_time_minutes
    return result

print(solution())