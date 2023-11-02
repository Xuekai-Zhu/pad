def solution():
    """Cynthia has four times as many water balloons as her husband, Randy. Randy has only half as many water balloons as his daughter, Janice. If Janice throws all 6 of her water balloons at her father, how many water balloons does Cynthia have, which she could also choose to throw at Randy?"""
    # Calculate the number of water balloons Randy has
    randy_balloons = 6 * 2

    # Calculate the number of water balloons Cynthia has
    cynthia_balloons = randy_balloons * 4

    result = cynthia_balloons
    return result

print(solution())