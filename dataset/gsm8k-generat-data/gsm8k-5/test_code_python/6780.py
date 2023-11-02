def solution():
    dave_time = 10  # Dave can ride the merry-go-round for 10 minutes before getting sick
    chuck_time = 5 * dave_time  # Chuck can ride 5 times longer than Dave
    erica_time = 1.3 * chuck_time  # Erica can stay 30% longer than Chuck before getting sick

    result = erica_time
    return result

print(solution())