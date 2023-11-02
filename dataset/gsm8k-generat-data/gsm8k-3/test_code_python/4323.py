def solution():
    """Sandra's dog gave birth to 7 puppies. Her vet gave her 105 portions of formula to give to the puppies for 5 days. How many times a day should Sandra feed the puppies?"""
    # Define the number of puppies and portions of formula
    num_puppies = 7
    num_portions = 105

    # Calculate the total number of portions needed per day
    daily_portions = num_portions / 5

    # Calculate the number of portions needed per puppy per day
    puppy_portions = daily_portions / num_puppies

    # Display the number of times Sandra should feed the puppies per day
    result = puppy_portions
    return result

print(solution())