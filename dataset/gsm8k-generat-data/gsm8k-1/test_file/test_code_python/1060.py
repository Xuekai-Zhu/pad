def solution():
    """The Science Center hosted field trips Monday through Friday last week. On Monday, 32 classes visited. Twice as many visited on Tuesday and three times as many visited on Wednesday. Another 30 classes visited on Thursday and 25 visited on Friday. In all, how many classes visited the Science Center last week?"""
    monday_classes = 32
    tuesday_classes = monday_classes * 2
    wednesday_classes = monday_classes * 3
    thursday_classes = 30
    friday_classes = 25
    total_classes = monday_classes + tuesday_classes + wednesday_classes + thursday_classes + friday_classes
    result = total_classes
    return result

print(solution())