def solution():
    """James has five huskies, two pitbulls and four golden retrievers, all female. They became pregnant and each golden retriever had two more pups than each husky. If the huskies and pitbulls had 3 pups each, how many more pups than adult dogs are there in total?"""
    huskies = 5
    pitbulls = 2
    golden_retrievers = 4
    husky_pups = 3
    pitbull_pups = 3
    golden_retriever_pups = husky_pups + 2
    total_dogs = huskies + pitbulls + golden_retrievers
    total_pups = (huskies * husky_pups) + (pitbulls * pitbull_pups) + (golden_retrievers * golden_retriever_pups)
    more_pups = total_pups - total_dogs
    result = more_pups
    return result

print(solution())