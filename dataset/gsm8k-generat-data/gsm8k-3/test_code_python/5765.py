def solution():
    """Lily got a new puppy for her birthday.  She was responsible for feeding the puppy 1/4 cup of food three times a day for two weeks starting tomorrow.  For the following 2 weeks, Lily will feed him 1/2 cup of food twice a day.  She has fed him 1/2 cup of food today.  Including today, how much food will the puppy eat over the next 4 weeks?"""
    
    # Calculate the total amount of food for the first two weeks
    first_two_weeks = (1/4 * 3) * 14
    # Calculate the total amount of food for the last two weeks
    last_two_weeks = (1/2 * 2) * 14
    # Calculate the amount of food eaten today
    today = 1/2
    # Calculate the total amount of food eaten over four weeks
    total_food = first_two_weeks + last_two_weeks + today
    # Display the total amount of food
    result = total_food
    return result

print(solution())