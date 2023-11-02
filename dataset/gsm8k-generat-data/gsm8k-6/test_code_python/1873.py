def solution():
    # Determine Sebastian's age
    sebastian_age = 40 + 4  # Sebastian is 4 years older than Jeremy

    # Calculate the sum of their ages currently
    current_sum = 40 + sebastian_age + (sebastian_age - 4)  # Sophia is currently 4 years younger than Sebastian

    # Calculate the total sum of their ages after three years
    future_sum = current_sum + 3*3  # adding three years as given in the question

    # Calculate Sophia's age three years from now
    sophia_age = future_sum - 40 - (sebastian_age + 3)  # subtracting Jeremy's and Sebastian's age, and adding 3 years to Sophia's current age

    result = sophia_age
    return result

print(solution())