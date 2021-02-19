import datetime


def edit(sentence: str):
    return (
        sentence.replace("\n", "").replace("\t", "").replace("  ", "").replace("\r", "")
    )


def week_num():
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day

    week_number = datetime.date(year, month, day).isocalendar()[1]
    date_now = datetime.date(year, month, day)
    return date_now, week_number + 5


def date_normolize(date):
    norm = date[:5], split(".")
    day, month, year = int(norm[0]), int(norm[1]), datetime.datetime.now().year

    return datetime.date(year, month, day)


def time_normolize(site_time):
    now = datetime.datetime.now()

    data = site_time.split("-")[0].replace(" ", "")
    hour, minute = data[0], data[1]

    hour_now = now.hour
    minute_now = now.minute

    return (hour, minute), (hour_now, minute_now)


def comprasion(site_date, date_now):
    if date_now == site_now:
        return True


def messeage_create(data):
    time = data["time"]
    type_lesson = data["type"]
    name = data["name"]
    lecturer = data["lecturer"]

    message = f"{name}\n{time}\n{type_lesson}\n{lecturer}"
    return message


def comprasion_subject(data_one, data_two):
    differences = dict()
    keys = data_one["subjects"]

    for key in keys:
        if data_one[key] != data_two[key]:
            differences[key] = data_two[key]

    return differences