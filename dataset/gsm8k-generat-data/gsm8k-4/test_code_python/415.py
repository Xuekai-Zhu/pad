def solution():
    """Bert's golden retriever has grown tremendously since it was a puppy. At 7 weeks old, the puppy weighed 6 pounds, but doubled in weight by week 9. It doubled in weight again at 3 months old, and doubled again at 5 months old. Finally, the dog reached its final adult weight by adding another 30 pounds by the time it was one year old. What is the dog's full adult weight, in pounds?"""
    # Define the initial weight of the puppy
    puppy_weight = 6

    # Calculate the weight at 9 weeks
    puppy_weight *= 2

    # Calculate the weight at 3 months
    puppy_weight *= 2

    # Calculate the weight at 5 months
    puppy_weight *= 2

    # Add the final 30 pounds to reach adult weight
    adult_weight = puppy_weight + 30

    # return the result
    result = adult_weight
    return result

print(solution())