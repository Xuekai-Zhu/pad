def solution():
    puppies_adopted_week_one = 20
    puppies_adopted_week_two = (2/5) * puppies_adopted_week_one
    puppies_adopted_week_three = 2 * puppies_adopted_week_two
    puppies_adopted_week_four = puppies_adopted_week_one + 10
    total_puppies = puppies_adopted_week_one + puppies_adopted_week_two + puppies_adopted_week_three + puppies_adopted_week_four
    result = total_puppies
    return result

print(solution())