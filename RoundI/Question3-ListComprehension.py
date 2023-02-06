from datetime import datetime, timedelta
import calendar

def compute_prev_date(dates_list:list):
    """
    """
    #Creating an empty array
    prev_dates = []

    #for loop to perform all computations
    for date in dates_list:
        date_object = datetime.strptime(date, '%Y-%m-%d')

        prev_date = date_object - timedelta(days=1)

        month_abbr = calendar.month_abbr[prev_date.month]

        prev_dates.append(f"{prev_date.day } {month_abbr} { prev_date.year}")

    return prev_dates
#outputting the results
print(compute_prev_date(['1999-01-21']))
print(compute_prev_date(['1999-01-21','2022-03-01','2099-11-21']))
print(compute_prev_date(['2022-11-01','2022-11-02']))