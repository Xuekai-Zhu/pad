def solution():
    # Calculate the total boring hours of gameplay and subtract them from the total gameplay to find the enjoyable gameplay hours
    total_gameplay = 100  # hours of promised gameplay
    boring_hours = 0.8 * total_gameplay  # 80% of the gameplay is boring
    enjoyable_hours = total_gameplay - boring_hours + 30  # add 30 hours of enjoyable gameplay from the expansion
    result = enjoyable_hours
    return result

print(solution())