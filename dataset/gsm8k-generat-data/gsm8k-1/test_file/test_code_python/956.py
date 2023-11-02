Unfortunately, we cannot provide a solution to the Samantha's last name question as it is incomplete and missing crucial information. 

As for the pirate crew question:

def solution():
    """A pirate crew is digging for buried treasure on the island marked X on a map. They dug ten holes the first day, thirteen holes the second day, and eight holes the third day. They stopped digging early on the third day to fill in two holes the pirates kept falling in. On the fourth day of digging, they unearthed a treasure chest full of gold, jewels, and an aged hat. The island had four times as many holes by then as it did at the end of the first day. How many holes did the pirates dig on the fourth day before finding the treasure?"""
    holes_day1 = 10
    holes_day2 = 13
    holes_day3 = 8
    holes_filled = 2
    total_holes = (holes_day1 + holes_day2 + holes_day3 - holes_filled) * 4
    holes_first_day = holes_day1
    holes_fourth_day = total_holes / 4 - holes_first_day - holes_day2 - holes_day3
    result = holes_fourth_day
    return result

print(solution())