def solution():
    # Calculate the number of golden retriever pups
    husky_pups = 3 * 5
    total_golden_retriever_pups = (4 * (2 + husky_pups))

    # Calculate the total number of pups and adult dogs
    total_pups = total_golden_retriever_pups + 3 * (5 + 2)
    total_adult_dogs = 5 + 2 + 4

    # Calculate the difference between the number of pups and adult dogs
    diff = total_pups - total_adult_dogs

    result = diff
    return result

print(solution())