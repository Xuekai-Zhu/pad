def solution():
    """They say the first year of a dog's life equals 15 human years. The second year of a dog's life equals 9 human years and after that, every year of a dog's life equals 5 human years. According to this logic, how many human years has my 10-year-old dog lived?"""
    # Define the age of the dog
    dog_age = 10

    # Calculate the human age equivalent for the first two years of the dog's life
    human_age = 15 + 9

    # Calculate the human age equivalent for the remaining years of the dog's life
    remaining_years = dog_age - 2
    human_age += remaining_years * 5

    # return the result
    result = human_age
    return result

print(solution())