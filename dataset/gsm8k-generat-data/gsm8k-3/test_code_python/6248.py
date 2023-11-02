def solution():
    """James has five huskies, two pitbulls and four golden retrievers, all female. They became pregnant and each golden retriever had two more pups than each husky. If the huskies and pitbulls had 3 pups each, How many more pups than adult dogs are there in total?"""
    # Define the number of adult dogs
    huskies = 5
    pitbulls = 2
    golden_retrievers = 4

    # Define the number of pups per litter
    husky_pups = 3
    pitbull_pups = 3
    golden_retriever_pups = husky_pups + 2

    # Calculate the total number of pups
    total_pups = (huskies + pitbulls) * husky_pups + golden_retrievers * golden_retriever_pups

    # Calculate the number of adult dogs
    total_adult_dogs = huskies + pitbulls + golden_retrievers

    # Calculate the difference between the total number of pups and the number of adult dogs
    difference = total_pups - total_adult_dogs

    # Display the result
    result = difference
    return result

print(solution())