import datetime as dt

def daterange(date1, date2):
    for n in range(delta.days):
        yield date1 + dt.timedelta(n)

def test1():
    today = dt.datetime.today()

    print(today)

    year = 2028
    date0 = dt.date(year, 1, 1)
    date1 = dt.date(year+1, 1, 1)
    delta = date1 - date0

    print(delta)


    date_list = []
    for d in daterange(date0, date1):
        date_str = d.strftime("%d.%m.%Y")
        date_list.append(date_str)
    print(len(date_list))

###################
def calender_generator(year=2022):
    dates = {}
    if year == None:
        return "None"
    else:
        date0 = dt.date(year, 1, 1)
        date1 = dt.date(year+1, 1, 1)
        for d in daterange(date0, date1):
            num_of_week = int(d.strftime("%W"))
            num_of_day = d.strftime("%j")
            date_str = d.strftime("%d.%m.%Y")
            num_of_week_day = int(d.strftime("%w"))
            if num_of_week_day == 0:
                num_of_week_day = 7
            #dates[num_of_week] = {}
            dates[num_of_week][num_of_week_day] = {
                    "num_of_day": num_of_day,
                    "date_str": date_str
                }

        print(dates)
        return dates

def calender_generator2(year=2022):
    start_date = dt.date(year, 1, 1)
    end_date = dt.date(year+1, 1, 1)
    delta = end_date - start_date

    day_lst = [start_date + dt.timedelta(days=x) for x in range(delta.days)]
    week_dct = {}

    for day in day_lst:
        num_of_week = int(day.strftime("%W"))
        week_dct[num_of_week] = {}
    for day in day_lst:
        num_of_week = int(day.strftime("%W"))
        num_of_week_day = int(day.strftime("%w"))
        if num_of_week_day == 0:
            num_of_week_day = 7
        num_of_day = int(day.strftime("%j"))
        date_str = day.strftime("%d.%m.%Y")
        week_dct[num_of_week][num_of_week_day] = {
            "num_of_day": num_of_day,
            "date_str": date_str
        }

    return week_dct

#calender = calender_generator2(2022)
#print(calender[2])

def find_largest_element(numbers):
    largest = None
    for number in numbers:
        if largest is None or number > largest:
            largest = number
    return largest

print(find_largest_element([1, 2, 3, -7]))
print(find_largest_element([4, 3, 2, 1]))
print(find_largest_element([1, 1, 1, 1]))
print(find_largest_element([]))

def find_smallest_element(numbers):
    smallest = None
    for number in numbers:
        if smallest is None or number < smallest:
            smallest = number
    return smallest

print(find_smallest_element([1, 2, 3, 4]))
print(find_smallest_element([4, 3, 2, 1]))
print(find_smallest_element([1, 1, 1, 1]))
print(find_smallest_element([-1, -2, -3, -4]))
print(find_smallest_element([]))

