def solution():
    # Define the hourly rates and hours worked
    housesit_rate = 15
    dog_walk_rate = 22
    housesit_hours = 10
    dog_walk_hours = 3

    # Calculate the earnings from each job
    housesit_earnings = housesit_rate * housesit_hours
    dog_walk_earnings = dog_walk_rate * dog_walk_hours

    # Calculate the total earnings
    total_earnings = housesit_earnings + dog_walk_earnings
    result = total_earnings
    return result

print(solution())