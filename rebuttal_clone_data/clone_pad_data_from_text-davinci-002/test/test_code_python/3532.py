def solution():
    number_huskies = 5
    number_pitbulls = 2
    number_golden_retrievers = 4
    total_adult_dogs = number_huskies + number_pitbulls + number_golden_retrievers
    husky_pups = number_huskies * 3
    pitbull_pups = number_pitbulls * 3
    golden_retriever_pups = number_golden_retrievers * 5
    total_pups = husky_pups + pitbull_pups + golden_retriever_pups
    result = total_pups - total_adult_dogs
    return result

print(solution())