def solution():
    """Alex has not washed his clothes for a month; 18 shirts, 12 pants, 17 sweaters, and 13 jeans are waiting to be washed. Alex's washing machine can wash a maximum of 15 items per cycle. Each cycle takes 45 minutes. How many hours will it take the washing machine to wash all the clothes?"""
    # Define the number of items waiting to be washed
    shirts = 18
    pants = 12
    sweaters = 17
    jeans = 13

    # Calculate the total number of items waiting to be washed
    total_items = shirts + pants + sweaters + jeans

    # Calculate the number of cycles needed to wash all the items
    cycles = total_items // 15
    if total_items % 15 != 0:
        cycles += 1

    # Calculate the time needed to wash all the items
    time = cycles * 45 / 60

    # Display the time needed to wash all the items
    result = time
    return result

print(solution())