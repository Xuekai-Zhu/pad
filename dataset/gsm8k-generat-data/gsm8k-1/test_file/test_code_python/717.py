def solution():
    """Helga was the fastest clog dancer in all of Slovenia. With both hands at her sides, she could tap her right foot at a rate of 300 taps per minute, while simultaneously tapping her left foot at a rate of 250 taps per minute. When she raised her arms, her tap rate slowed down to 200 taps per minute with each foot. If she dances a total of 5 minutes, with her arms raised during only 2 of those minutes, what would be the combined total number of times that she taps both of her feet?"""
    hands_down_rate = 550
    hands_up_rate = 400
    total_time = 5
    hands_down_time = total_time - 2
    hands_up_time = 2
    total_taps = (hands_down_rate * hands_down_time) + (hands_up_rate * hands_up_time)
    result = total_taps
    
    return result

print(solution())