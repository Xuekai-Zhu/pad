def solution():
    """Billy weighs 9 pounds more than Brad. Brad weighs 5 pounds more than Carl. If Carl weighs 145 pounds, how much does Billy weigh, in pounds?"""
    # Define Carl's weight
    carl_weight = 145

    # Calculate Brad's weight
    brad_weight = carl_weight + 5

    # Calculate Billy's weight
    billy_weight = brad_weight + 9
    
    result = billy_weight
    return result

print(solution())