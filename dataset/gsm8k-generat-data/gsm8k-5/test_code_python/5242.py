def solution():
    willy_initial = 10  # Willy has 10 stuffed animals to start with
    willy_birthday = 2  # Willy gets 2 more stuffed animals for his birthday
    willy_total = willy_initial + willy_birthday  # Willy's total number of stuffed animals after his birthday
    dad_gift = 3 * willy_total  # Willy's dad gives him 3 times more stuffed animals than he has

    # Calculate Willy's total number of stuffed animals
    total_stuffed_animals = willy_total + dad_gift
    result = total_stuffed_animals
    return result

print(solution())