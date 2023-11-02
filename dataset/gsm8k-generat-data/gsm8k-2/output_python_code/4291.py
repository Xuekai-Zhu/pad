def solution():
    """Jordan and Perry took a boat out to the lake to go fishing on a Monday morning. Jordan caught 4 fish and Perry caught double what Jordan caught. On the way back to shore, the boat tipped over and they lost one-fourth of their total catch. How many fish remain?"""
    jordan_catch = 4
    perry_catch = jordan_catch * 2
    total_catch = jordan_catch + perry_catch
    lost_catch = total_catch / 4
    remaining_catch = total_catch - lost_catch
    result = remaining_catch
    return result

print(solution())