def solution():
    total_gameplay = 100  # James is promised 100 hours of gameplay in the new game
    boring_gameplay = total_gameplay * 0.8  # 80% of the gameplay is boring grinding
    enjoyable_gameplay = total_gameplay - boring_gameplay  # Calculate the enjoyable gameplay
    enjoyable_gameplay += 30  # Add the additional 30 hours of enjoyable gameplay from the expansion
    result = enjoyable_gameplay
    return result

print(solution())