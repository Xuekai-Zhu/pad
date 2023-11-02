def solution():
    workout_days = 3  # Geli is committed to 3 workout days per week
    starting_pushups = 10  # Geli starts with 10 push-ups on her first day
    pushup_increment = 5  # Geli adds 5 push-ups each day

    # Calculate the total number of push-ups Geli will do in her first week
    total_pushups = starting_pushups + (pushup_increment * (workout_days - 1)) + starting_pushups + (
                pushup_increment * (workout_days - 1)) + starting_pushups + (pushup_increment * (workout_days - 1))

    result = total_pushups
    return result

print(solution())