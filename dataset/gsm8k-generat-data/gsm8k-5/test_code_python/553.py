def solution():
    milk_containers_per_day = 2  # Emma buys 2 containers of milk every school day
    days_per_week = 5  # Emma goes to school for 5 days in a week
    weeks = 3  # Emma wants to know how many containers of milk she buys in 3 weeks

    # Calculate the total number of milk containers Emma buys in 3 weeks
    total_milk_containers = milk_containers_per_day * days_per_week * weeks

    result = total_milk_containers
    return result

print(solution())