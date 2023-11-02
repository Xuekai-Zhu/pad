def solution():
    num_huskies = 5
    num_pitbulls = 2
    num_golden_retrievers = 4
    extra_pups_per_golden_retriever = 2
    num_pups_per_husky = 3

    # Calculate the total number of adult dogs
    total_adult_dogs = num_huskies + num_pitbulls + num_golden_retrievers

    # Calculate the number of pups for each golden retriever
    num_pups_per_golden_retriever = num_pups_per_husky + extra_pups_per_golden_retriever

    # Calculate the total number of golden retriever pups
    total_golden_retriever_pups = num_golden_retrievers * num_pups_per_golden_retriever

    # Calculate the total number of husky and pitbull pups
    total_husky_and_pitbull_pups = (num_huskies + num_pitbulls) * num_pups_per_husky

    # Calculate the total number of pups
    total_pups = total_golden_retriever_pups + total_husky_and_pitbull_pups

    # Calculate the difference between the total number of pups and adult dogs
    difference = total_pups - total_adult_dogs

    result = difference
    return result

print(solution())