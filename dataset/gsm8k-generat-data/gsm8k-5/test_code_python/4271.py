def solution():
    total_time_away = 32  # Dante has been away from the Park Office for 32 minutes in total
    time_to_hidden_lake = 15  # It takes Dante 15 minutes to walk to Hidden Lake from the Park Office
    time_from_hidden_lake_to_office = 7  # It takes Dante 7 minutes to walk back from Hidden Lake to the Park Office

    # Calculate the time Dante spent at Hidden Lake
    time_at_hidden_lake = total_time_away - time_to_hidden_lake - time_from_hidden_lake_to_office

    # Calculate the time Dante took to walk to the restaurant from the Park Office before going to Hidden Lake
    time_to_restaurant = (time_at_hidden_lake + time_to_hidden_lake) / 2

    # Calculate the time it takes to walk from the Park Office to the Lake Park restaurant
    time_from_office_to_restaurant = time_to_restaurant - time_to_hidden_lake

    result = time_from_office_to_restaurant
    return result

print(solution())