def solution():
    couples = 3
    singles = 5
    total_members = couples*2 + singles + 2  # adding Ron and his wife

    # Since each member gets to pick a new book every week, Ron gets to pick 1/total_members times per week
    # Multiply by 52 to get the number of times per year
    ron_picks = (1/total_members) * 52

    result = ron_picks
    return result

print(solution())