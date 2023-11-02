def solution():
    """Bert's golden retriever has grown tremendously since it was a puppy.  At 7 weeks old, the puppy weighed 6 pounds, but doubled in weight by week 9.  It doubled in weight again at 3 months old, and doubled again at 5 months old.  Finally, the dog reached its final adult weight by adding another 30 pounds by the time it was one year old.  What is the dog's full adult weight, in pounds?"""
    # Define the puppy's initial weight and the ages at which it doubled in weight
    init_weight = 6
    week9 = 9
    month3 = 12
    month5 = 20

    # Calculate the dog's weight at each milestone
    weight_week9 = init_weight * 2
    weight_month3 = weight_week9 * 2
    weight_month5 = weight_month3 * 2
    weight_1year = weight_month5 + 30

    # Display the dog's full adult weight
    result = weight_1year
    return result

print(solution())