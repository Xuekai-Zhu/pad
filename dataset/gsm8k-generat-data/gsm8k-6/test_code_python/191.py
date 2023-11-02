def solution():
    # Calculate the number of weasels and rabbits caught by the foxes after 3 weeks
    weasels_caught = 3 * 4 * 3  # 3 foxes each catch 4 weasels per week for 3 weeks
    rabbits_caught = 3 * 2 * 3  # 3 foxes each catch 2 rabbits per week for 3 weeks

    # Calculate the number of weasels and rabbits remaining after the foxes hunt
    remaining_weasels = 100 - weasels_caught
    remaining_rabbits = 50 - rabbits_caught

    result = (remaining_weasels, remaining_rabbits)
    return result

print(solution())