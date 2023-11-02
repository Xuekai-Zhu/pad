def solution():
    """It takes 2.5 hours to groom a dog and 0.5 hours to groom a cat. What is the number of minutes it takes to groom 5 dogs and 3 cats?"""
    dog_groom_time = 2.5 * 60  # convert hours to minutes
    cat_groom_time = 0.5 * 60  # convert hours to minutes
    total_time = (5 * dog_groom_time) + (3 * cat_groom_time)
    result = total_time
    return result

print(solution())