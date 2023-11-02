def solution():
    # Calculate the total number of fish caught by all three
    ryan_catch = 3 * jason_catch  # Ryan caught three times the number of fish that Jason caught
    jeffery_catch = 60  # Jefferey caught 60 fish
    total_catch = jason_catch + ryan_catch + jeffery_catch  # Total number of fish caught by all three
    result = total_catch
    return result

print(solution())