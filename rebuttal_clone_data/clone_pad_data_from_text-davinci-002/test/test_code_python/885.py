def solution():
    initial_bug_population = 400
    percent_reduction = 80
    reduction_factor = percent_reduction / 100
    post_spray_population = initial_bug_population * reduction_factor
    spiders_introduced = 12
    bugs_eaten_per_spider = 7
    total_bugs_eaten = spiders_introduced * bugs_eaten_per_spider
    final_bug_population = post_spray_population - total_bugs_eaten
    result = final_bug_population
    return result

print(solution())