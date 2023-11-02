def solution():
    weight_to_lose = 5  # Jamie's father wants to lose 5 pounds
    calories_in_pound = 3500  # There are 3,500 calories in a pound of body fat
    caloric_deficit_per_day = 500  # Jamie's father needs to consume 500 fewer calories than he burns per day to lose 1 pound a week
    calories_burned_per_day = 2500  # Jamie's father burns 2,500 calories of fat a day by doing light exercise
    calories_consumed_per_day = 2000  # Jamie's father sticks to eating 2000 calories a day

    # Calculate the number of calories burned per day beyond what Jamie's father is eating
    caloric_deficit_per_day = calories_burned_per_day - calories_consumed_per_day

    # Calculate the number of days it will take for Jamie's father to burn off 5 pounds
    days_to_lose_weight = (weight_to_lose * calories_in_pound) / (caloric_deficit_per_day * 7) 

    result = days_to_lose_weight
    return result

print(solution())