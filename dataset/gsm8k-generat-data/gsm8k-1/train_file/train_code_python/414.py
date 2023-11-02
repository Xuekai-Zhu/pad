def solution():
    """Bert's golden retriever has grown tremendously since it was a puppy. At 7 weeks old, the puppy weighed 6 pounds, but doubled in weight by week 9. It doubled in weight again at 3 months old, and doubled again at 5 months old. Finally, the dog reached its final adult weight by adding another 30 pounds by the time it was one year old. What is the dog's full adult weight, in pounds?"""
    initial_weight = 6
    week_9_weight = initial_weight * 2
    month_3_weight = week_9_weight * 2
    month_5_weight = month_3_weight * 2
    adult_weight = month_5_weight + 30
    result = adult_weight
    return result

print(solution())