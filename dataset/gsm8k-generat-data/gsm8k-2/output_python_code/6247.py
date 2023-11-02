def solution():
    """James has five huskies, two pitbulls and four golden retrievers, all female. They became pregnant and each golden retriever had two more pups than each husky. If the huskies and pitbulls had 3 pups each, How many more pups than adult dogs are there in total?"""
    huskies = 5
    pitbulls = 2
    golden_retrievers = 4
    husky_pups = 3
    pitbull_pups = 3
    golden_retriever_pups = (huskies + golden_retrievers) * 2
    total_adult_dogs = huskies + pitbulls + golden_retrievers
    total_pups = husky_pups * huskies + pitbull_pups * pitbulls + golden_retriever_pups * golden_retrievers
    more_pups_than_dogs = total_pups - total_adult_dogs
    result = more_pups_than_dogs
    return result

print(solution())