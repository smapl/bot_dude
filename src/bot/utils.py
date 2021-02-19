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
    return week_number + 5
