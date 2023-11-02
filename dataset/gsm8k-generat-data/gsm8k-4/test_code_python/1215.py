def solution():
    """One US cup equals 250ml. Brian is making lasagna for himself, his wife, his two kids, his parents, and his wife's parents. The recipe requires 1/2 a cup of milk per serving. How many 1L cartons of milk does Brian need to buy if each person is expected to eat 2 servings?"""
    # Define the number of people Brian is cooking for
    num_people = 7

    # Define the number of servings per person
    servings_per_person = 2

    # Define the amount of milk needed per serving in liters
    milk_per_serving = 0.5 * 0.25

    # Calculate the total amount of milk needed in liters
    total_milk = num_people * servings_per_person * milk_per_serving

    # Calculate the number of 1L cartons of milk needed
    cartons = total_milk / 1

    result = round(cartons)
    return result

print(solution())