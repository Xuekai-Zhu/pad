def solution():
    # Define the time it takes to clip one cat's nails
    nail_time = 10

    # Define the time it takes to clean one ear
    ear_time = 90

    # Define the time it takes to shampoo the cat
    shampoo_time = 5*60

    # Calculate the total time to groom one cat
    cat_grooming_time = (4 * nail_time) + ear_time + shampoo_time

    result = cat_grooming_time
    return result

print(solution())