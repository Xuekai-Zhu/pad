def solution():
    # Calculate the total number of suckers
    total_suckers = 2 * (2 * (2 * (3 + 5) + 1) + 5)  # Sienna gives half to Bailey, Jen eats half, Molly eats 2 and gives the rest to Harmony, Harmony keeps 3 and passes the remainder to Taylor, Taylor eats one and gives the last 5 to Callie
    # Calculate the number of suckers that Jen ate
    jen_suckers = total_suckers // 8  # Jen ate half of the original total, which is 1/4 of the final total after all the sharing
    result = jen_suckers
    return result

print(solution())