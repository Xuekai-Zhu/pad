def solution():
    """One US cup equals 250ml. Brian is making lasagna for himself, his wife, his two kids, his parents, and his wife's parents. The recipe requires 1/2 a cup of milk per serving. How many 1L cartons of milk does Brian need to buy if each person is expected to eat 2 servings?"""
    # Define the volume of one serving of milk
    MILK_PER_SERVING = 0.5  # cup

    # Define the number of people Brian is cooking for
    NUM_PEOPLE = 6

    # Define the number of servings needed (2 per person)
    NUM_SERVINGS = 2 * NUM_PEOPLE

    # Calculate the total volume of milk needed in ml
    total_milk_volume = NUM_SERVINGS * MILK_PER_SERVING * 250

    # Calculate the number of 1L cartons of milk needed
    num_cartons = int(total_milk_volume / 1000) + 1

    # Display the number of cartons needed
    result = num_cartons
    return result

print(solution())