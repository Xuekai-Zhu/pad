def solution():
    """Cynthia has four times as many water balloons as her husband, Randy. Randy has only half as many water balloons as his daughter, Janice. If Janice throws all 6 of her water balloons at her father, how many water balloons does Cynthia have, which she could also choose to throw at Randy?"""
    # Define the number of balloons Janice has
    janice_balloons = 6

    # Calculate the number of balloons Randy has
    randy_balloons = janice_balloons * 2

    # Calculate the number of balloons Cynthia has
    cynthia_balloons = randy_balloons * 4

    # Display the number of balloons Cynthia could throw at Randy
    result = cynthia_balloons
    return result

print(solution())