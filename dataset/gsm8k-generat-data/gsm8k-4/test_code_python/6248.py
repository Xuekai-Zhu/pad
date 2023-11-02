def solution():
    """James has five huskies, two pitbulls and four golden retrievers, all female. They became pregnant and each golden retriever had two more pups than each husky. If the huskies and pitbulls had 3 pups each, How many more pups than adult dogs are there in total?"""
    # Define the initial number of dogs
    huskies = 5
    pitbulls = 2
    golden_retrievers = 4

    # Calculate the total number of adult dogs
    adult_dogs = huskies + pitbulls + golden_retrievers

    # Calculate the number of puppies for each type of dog
    husky_pups = huskies * 3
    pitbull_pups = pitbulls * 3
    golden_retriever_pups = (golden_retrievers * 2) + huskies * 2

    # Calculate the total number of puppies
    total_pups = husky_pups + pitbull_pups + golden_retriever_pups

    # Calculate the difference between the number of puppies and the number of adult dogs
    difference = total_pups - adult_dogs

    # return the result
    result = difference
    return result

print(solution())