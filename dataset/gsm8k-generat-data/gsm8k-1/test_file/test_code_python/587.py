def solution():
    """Four dogs sat in a line within the veterinarian's waiting room. The first dog was the Affenpinscher, who weighed only 10 pounds. Next to him sat a Dachshund, who weighed twice as much as the Affenpinscher. Next to the Dachshund sat a Papillon, who weighed one-fourth as much as the Dachshund. And at the end of the line sat a Mastiff, who weighed 44 times the weight of the Papillon. How much did the Mastiff weigh, in pounds?"""
    affenpinscher_weight = 10
    dachshund_weight = affenpinscher_weight * 2
    papillon_weight = dachshund_weight / 4
    mastiff_weight = papillon_weight * 44
    result = mastiff_weight
    return result

print(solution())