def solution():
    # Define the number of push-ups Miriam does each day
    monday_pushups = 5
    tuesday_pushups = 7
    wednesday_pushups = 2 * tuesday_pushups
    thursday_pushups = (monday_pushups + tuesday_pushups + wednesday_pushups) / 2
    friday_pushups = monday_pushups + tuesday_pushups + wednesday_pushups + thursday_pushups

    result = friday_pushups
    return result

print(solution())