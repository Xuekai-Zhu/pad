def solution():
    
    # Define the number of widgets produced by the Widgeteer and the WidgetMaster
    widget_rate = 60
    widget_rate_master = 45

    # Define the number of hours worked by the WidgetMaster in a month
    hours_per_month = 24 * 30

    # Calculate the total number of widgets produced by the WidgetMaster in a month
    widgets_per_month = widget_rate * hours_per_month

    # Calculate the total number of widgets produced by the Widgeteer and the WidgetMaster in a month
    widgets_to_buy = widget_rate * widgets_per_month

    # Calculate the difference in the number of widgets produced
    difference = widgets_to_buy - widgets_to_buy

    # return the result
    result = difference
    return result

print(solution())