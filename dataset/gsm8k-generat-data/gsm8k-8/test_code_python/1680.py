def solution():
    # Define the total number of pieces of candy
    total_candy = 349

    # Define the number of pieces taken by Talitha and Solomon
    talitha_candy = 108
    solomon_candy = 153

    # Calculate the number of pieces remaining in the bowl
    remaining_candy = total_candy - talitha_candy - solomon_candy
    result = remaining_candy
    return result

print(solution())