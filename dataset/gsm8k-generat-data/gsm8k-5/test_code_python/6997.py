def solution():
    cupcakes_on_thursday = 1200  # Kim sold 1200 boxes on Thursday
    cupcakes_on_wednesday = cupcakes_on_thursday / 2  # Kim sold half as many on Wednesday
    cupcakes_on_tuesday = cupcakes_on_wednesday * 2  # Kim sold twice as many on Tuesday

    result = cupcakes_on_tuesday
    return result

print(solution())