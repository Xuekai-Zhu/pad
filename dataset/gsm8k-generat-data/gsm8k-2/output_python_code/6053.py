def solution():
    """There were 20 fishermen in the lake who had cast their net to catch fish. If they caught 10000 fish in total, and 19 of them caught 400 fish each with their own net, calculate the number of fish the twentieth fisherman caught."""
    total_fishermen = 20
    total_fish_caught = 10000
    fish_caught_per_person = 400
    fish_caught_by_nineteen = 19 * fish_caught_per_person
    fish_caught_by_twentieth = total_fish_caught - fish_caught_by_nineteen
    result = fish_caught_by_twentieth
    return result

print(solution())