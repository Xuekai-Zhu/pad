def solution():
    """Amalia, Megan, and Dior divided the home chores so that each person had something to do while the others were working. Amalia's work was to mow the lawn, which took her 4 hours. Megan had to walk the dog and this took her 2 hours longer than Amalia to complete her chore. Dior's work was to do laundry and she took well over 4 hours longer than the time Amalia took to mow the lawn. Calculate the total time they all took to do their chores altogether."""
    amalia_time = 4
    megan_time = amalia_time + 2
    dior_time = amalia_time + 4
    total_time = amalia_time + megan_time + dior_time
    result = total_time
    return result

print(solution())