def solution():
    # Calculate the total amount contributed by everyone
    total_contribution = 100 - 15 - (2 * 15)  # boss contributes $15 and Todd contributes twice as much as the boss
    remaining_people = 5  # Nick and 4 other employees
    each_contribution = total_contribution / remaining_people  # divide the remaining contribution equally among the 5 people
    
    result = each_contribution
    return result

print(solution())