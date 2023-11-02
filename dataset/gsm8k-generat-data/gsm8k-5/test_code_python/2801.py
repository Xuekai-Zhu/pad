def solution():
    legs_seen = 12 * 2 + 8 * 4 + 5 * 4  # Borgnine has already seen 12 chimps (2 legs each), 8 lions (4 legs each), and 5 lizards (4 legs each)
    legs_goal = 1100  # Borgnine wants to see a total of 1100 legs at the zoo

    # Calculate the number of tarantulas Borgnine needs to see to meet his goal
    tarantulas_needed = (legs_goal - legs_seen) / 8

    result = tarantulas_needed
    return result

print(solution())