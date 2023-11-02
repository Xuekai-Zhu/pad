def solution():
    num_seashells_this_week = 50
    additional_seashells_per_week = 20
    num_weeks_in_month = 4

    total_seashells = num_seashells_this_week
    for i in range(1, num_weeks_in_month):
        additional_seashells = additional_seashells_per_week * i
        total_seashells += (num_seashells_this_week + additional_seashells)

    result = total_seashells
    return result

print(solution())