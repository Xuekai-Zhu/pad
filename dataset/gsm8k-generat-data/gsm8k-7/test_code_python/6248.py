def solution():
    num_huskies = 5
    num_pitbulls = 2
    num_golden_retrievers = 4

    husky_pup_count = 3
    pitbull_pup_count = 3

    # Calculate the total number of pups from the huskies and pitbulls
    total_pup_count = (num_huskies + num_pitbulls) * husky_pup_count

    # Calculate the number of pups each golden retriever had
    num_pups_per_golden_retriever = husky_pup_count + 2

    # Calculate the total number of pups from the golden retrievers
    total_golden_retriever_pup_count = num_golden_retrievers * num_pups_per_golden_retriever

    # Calculate the total number of dogs and pups
    total_dogs_and_pups = num_huskies + num_pitbulls + num_golden_retrievers + total_pup_count + total_golden_retriever_pup_count

    # Calculate the total number of extra pups
    extra_pup_count = total_pup_count + total_golden_retriever_pup_count - (num_huskies + num_pitbulls + num_golden_retrievers)

    result = extra_pup_count
    return result

print(solution())