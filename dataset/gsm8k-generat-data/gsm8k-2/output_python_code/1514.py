def solution():
    """Billy weighs 9 pounds more than Brad. Brad weighs 5 pounds more than Carl. If Carl weighs 145 pounds, how much does Billy weigh, in pounds?"""
    carl_weight = 145
    brad_weight = carl_weight + 5
    billy_weight = brad_weight + 9
    result = billy_weight
    return result

print(solution())