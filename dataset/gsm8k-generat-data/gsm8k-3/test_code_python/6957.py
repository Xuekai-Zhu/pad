def solution():
    """They say the first year of a dog's life equals 15 human years. The second year of a dog's life equals 9 human years and after that, every year of a dog's life equals 5 human years. According to this logic, how many human years has my 10-year-old dog lived?"""
    # Define the age of the dog
    dog_age = 10

    # Calculate the human equivalent age of the dog
    human_age = 0
    if dog_age == 1:
        human_age = 15
    elif dog_age == 2:
        human_age = 24
    else:
        human_age = 24 + (dog_age - 2) * 5

    # Display the human equivalent age of the dog
    result = human_age
    return result

print(solution())