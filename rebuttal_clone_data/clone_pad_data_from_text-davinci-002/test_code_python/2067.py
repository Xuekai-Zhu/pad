def solution():
    goal = 3000
    day_one = 600
    day_two = 900
    day_three = 400
    day_four = (day_one + day_two + day_three) / 2
    day_five = day_four / 2
    day_six = day_five / 2
    day_seven = day_six / 2
    day_eight = day_seven / 2
    money_needed = goal - (day_one + day_two + day_three + day_four + day_five + day_six + day_seven + day_eight)
    people = 6
    money_needed_per_person = money_needed / people
    result = money_needed_per_person

print(solution())