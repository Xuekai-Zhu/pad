def solution():
    # Calculate the total number of people who have disappeared and reappeared
    total_people = 0
    for i in range(100):
        if i % 10 == 0:  # one-tenth of the time, the audience member never reappears
            continue
        else:
            if i % 5 == 0:  # one-fifth of the time, two people reappear instead of only one
                total_people += 2
            else:
                total_people += 1
    result = total_people
    return result

print(solution())