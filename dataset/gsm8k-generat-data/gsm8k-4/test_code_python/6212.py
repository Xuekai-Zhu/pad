def solution():
    """Daragh had 20 stuffed bears. She took out her favorite 8 bears and then equally divided the other bears among her 3 sisters. Daragh's youngest sister, Eden, already had 10 stuffed bears. How many stuffed bears does Eden have now?"""
    # Define the initial number of stuffed bears
    initial_bears = 20

    # Define the number of bears Daragh kept as her favorite
    favorite_bears = 8

    # Calculate the number of bears left to divide among Daragh's sisters
    remaining_bears = initial_bears - favorite_bears

    # Calculate the number of bears each sister gets
    sister_bears = remaining_bears // 3

    # Calculate the number of bears Eden now has
    eden_bears = sister_bears + 10

    # return the result
    result = eden_bears
    return result

print(solution())