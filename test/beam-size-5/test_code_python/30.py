def solution():
    raymond_jewels = 40  # Raymond has 40 jewels
    aaron_jewels = (raymond_jewels / 2) + 5  # Aaron has 5 more jewels than half of Raymond's jewels
    Siobhan_jewels = aaron_jewels - 2  # Siobhan has 2 fewer jewels than Aaron

    result = Siobhan_jewels
    return result

print(solution())