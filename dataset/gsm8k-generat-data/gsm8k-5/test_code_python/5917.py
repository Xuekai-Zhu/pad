def solution():
    total_dogs = 80  # Harly's animal shelter has 80 dogs
    adopted_dogs = int(0.4 * total_dogs)  # 40% of the dogs are adopted out
    returned_dogs = 5  # 5 dogs were returned

    # Calculate the current number of dogs in the shelter
    current_dogs = total_dogs - adopted_dogs + returned_dogs
    result = current_dogs
    return result

print(solution())