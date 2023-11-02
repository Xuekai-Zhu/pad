def solution():
    # Calculate the total number of toys bought by Junior
    total_toys = 6 + 2*6 + 4*6 + (1/2)*2*6  # Monday: 6 toys, Wednesday: twice as many as Monday, Friday: four times as many as Monday, Saturday: half as many as Wednesday

    # Calculate the number of toys each rabbit would get
    toys_per_rabbit = total_toys / 16

    result = toys_per_rabbit
    return result

print(solution())