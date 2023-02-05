import datetime as dt
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thecodex'

YEARS = [2022, 2023]
NUM_TO_DAY = {
    1: "Mo",
    2: "Di",
    3: "Mi",
    4: "Do",
    5: "Fr",
    6: "Sa",
    7: "So"
}

class CalenderForm(FlaskForm):
    #https://www.youtube.com/watch?v=K2czdygI2wM
    date = StringField("date")
    unit = StringField("unit")
    note = StringField("note")
    submit = SubmitField("submit")


def calender_generator(year=2022):
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
        #num_of_day = int(day.strftime("%j"))
        date_str = day.strftime("%d.%m.%Y")
        week_dct[num_of_week][num_of_week_day-1] = date_str

    return week_dct


@app.route('/')
def main():
    return render_template('main.html', years=YEARS)


@app.route('/calender/')
@app.route('/calender/<int:year>', methods=['GET','POST'])
def calender(year=None):
    form = CalenderForm()
    return render_template(
        'calender.html',
        year=year, dates_dct=calender_generator(year),
        num_to_day=NUM_TO_DAY,
        form=form
    )


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(port=1337, debug=True)
