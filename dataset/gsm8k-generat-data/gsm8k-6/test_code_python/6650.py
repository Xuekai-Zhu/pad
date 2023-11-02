def solution():
    # Calculate the total number of bottles sold from Monday to Sunday
    total_bottles_sold = 2445 + 900 + 50*5  # Monday: 2445, Tuesday: 900, Wednesday to Sunday: 50*5

    # Calculate the number of bottles remaining after the sales
    bottles_remaining = 4500 - total_bottles_sold

    # Add the bottles delivered by the supplier on Saturday
    total_bottles = bottles_remaining + 650

    result = total_bottles
    return result

print(solution())