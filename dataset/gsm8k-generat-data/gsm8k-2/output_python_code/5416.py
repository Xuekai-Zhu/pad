def solution():
    """Mary tried to improve her health by changing her diet, but her weight bounced like a yo-yo. At first, she dropped a dozen pounds. Then, she added back twice the weight that she initially lost. Then, she dropped three times more weight than she initially had lost. But finally, she gained back half of a dozen pounds. If she weighed 99 pounds at the start of her change in diet, what was her final weight, in pounds?"""
    weight = 99
    weight -= 12
    weight += (2*12)
    weight -= (3*12)
    weight += (0.5*12)
    result = weight
    return result

print(solution())