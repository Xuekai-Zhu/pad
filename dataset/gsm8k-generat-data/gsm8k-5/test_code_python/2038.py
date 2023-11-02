def solution():
    time_per_woman = 50  # It takes 50 minutes to cut a woman's hair
    time_per_man = 15  # It takes 15 minutes to cut a man's hair
    time_per_kid = 25  # It takes 25 minutes to cut a kid's hair
    num_women = 3  # Joe cut 3 women's hair
    num_men = 2  # Joe cut 2 men's hair
    num_kids = 3  # Joe cut 3 children's hair

    # Calculate the total time Joe spent cutting hair
    total_time = time_per_woman * num_women + time_per_man * num_men + time_per_kid * num_kids
    result = total_time
    return result

print(solution())