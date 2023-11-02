def solution():
    # Calculate the total number of miles Benjamin walks in a week
    miles_to_work = 6 * 2 * 5  # Benjamin walks to work and back 5 days a week, which is 6 miles per trip
    miles_with_dog = 2 * 2 * 7  # Benjamin walks his dog twice a day, every day, which is 2 miles per walk
    miles_to_friend = 1 * 1  # Benjamin walks to his best friend's house once a week, which is 1 mile
    miles_to_store = 3 * 2  # Benjamin walks to the convenience store twice a week, which is 3 miles per trip
    total_miles = miles_to_work + miles_with_dog + miles_to_friend + miles_to_store
    result = total_miles
    return result

print(solution())