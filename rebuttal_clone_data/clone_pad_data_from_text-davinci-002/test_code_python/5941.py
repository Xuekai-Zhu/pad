def solution():
    milk_in_morning = 365
    milk_in_evening = 380
    milk_sold = 612
    milk_leftover = 15
    total_milk = milk_in_morning + milk_in_evening - milk_sold + milk_leftover
    result = total_milk
    return result

print(solution())