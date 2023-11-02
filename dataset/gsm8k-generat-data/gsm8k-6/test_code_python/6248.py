def solution():
    # Calculate the total number of adult dogs
    total_adult_dogs = 5 + 2 + 4  # five huskies, two pitbulls and four golden retrievers

    # Calculate the number of puppies each golden retriever had
    golden_puppies = 2 + 2*(2-1)  # each golden retriever had two more pups than each husky

    # Calculate the total number of puppies from the golden retrievers
    total_golden_puppies = 4 * golden_puppies  

    # Calculate the total number of puppies from the huskies and pitbulls
    total_husky_puppies = 5 * 3  # each husky had 3 puppies
    total_pitbull_puppies = 2 * 3  # each pitbull had 3 puppies

    # Calculate the total number of puppies
    total_puppies = total_golden_puppies + total_husky_puppies + total_pitbull_puppies  

    # Calculate the number of more pups than adult dogs
    more_pups = total_puppies - total_adult_dogs  
    result = more_pups
    return result

print(solution())