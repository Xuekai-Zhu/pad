def solution():
    """Siobhan has 2 fewer jewels than Aaron. Aaron has 5 more jewels than half of Raymond's jewels. If Raymond has 40 jewels, how many jewels does Siobhan have?"""
    raymond_jewels = 40
    aaron_jewels = (raymond_jewels / 2) + 5
    siobhan_jewels = aaron_jewels - 2
    result = siobhan_jewels
    return result

print(solution())