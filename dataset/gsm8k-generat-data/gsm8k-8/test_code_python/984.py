def solution():
    # Define the ratio of kangaroos to koalas
    kangaroo_to_koala_ratio = 5

    # Calculate the number of koalas
    koala_count = 180 // kangaroo_to_koala_ratio

    # Calculate the total number of animals
    animal_count = 180 + koala_count

    # Return the result as (koala count, animal count)
    result = (koala_count, animal_count)
    return result

print(solution())