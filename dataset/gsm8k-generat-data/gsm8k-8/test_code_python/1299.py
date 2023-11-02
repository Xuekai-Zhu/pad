def solution():
    # Define the number of weeds pulled on each day
    tuesday_weeds = 25
    wednesday_weeds = 3 * tuesday_weeds
    thursday_weeds = 1/5 * wednesday_weeds
    friday_weeds = thursday_weeds - 10

    # Calculate the total number of weeds pulled
    total_weeds = tuesday_weeds + wednesday_weeds + thursday_weeds + friday_weeds
    result = total_weeds
    return result

print(solution())