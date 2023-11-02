def solution():
    dog_years = 10

    # Calculate the human equivalent of the first two years of the dog's life
    human_years_first_two = 15 + 9

    # Calculate the human equivalent of the remaining years of the dog's life
    human_years_remaining = (dog_years - 2) * 5

    # Calculate the total human years that the dog has lived
    total_human_years = human_years_first_two + human_years_remaining
    result = total_human_years
    return result

print(solution())