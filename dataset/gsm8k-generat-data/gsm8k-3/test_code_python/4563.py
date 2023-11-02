def solution():
    """At the Mystic Aquarium, sharks are fed 4 buckets of fish each day. The dolphins are fed half as many buckets as the sharks while the other sea animals are fed 5 times as many buckets as the sharks. How many weeks will 546 buckets of fish last?"""
    # Define the number of buckets of fish per animal per day
    SHARK_FOOD = 4
    DOLPHIN_FOOD = SHARK_FOOD / 2
    OTHER_ANIMAL_FOOD = SHARK_FOOD * 5

    # Calculate the total number of buckets needed per day
    total_food = SHARK_FOOD + DOLPHIN_FOOD + OTHER_ANIMAL_FOOD

    # Calculate the number of days 546 buckets will last
    days = 546 / total_food

    # Calculate the number of weeks
    weeks = days / 7

    # Display the number of weeks
    result = weeks
    return result

print(solution())