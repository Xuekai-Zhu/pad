def solution():
    """Hannah slips on a banana peel and breaks her arm. The doctor charges her $200 for the cast, 
    $300/hour for a 30-minute visit, $4/pill for 30 painkillers, and $6/hour for a mandatory minimum of 2 hours of parking. 
    How much does the doctor's visit cost total?"""
    cast_cost = 200
    visit_cost = 300 * 0.5
    painkiller_cost = 4 * 30
    parking_cost = 6 * 2
    total_cost = cast_cost + visit_cost + painkiller_cost + parking_cost
    result = total_cost
    return result

print(solution())