import math
from datetime import date
import datetime as dt

class PredictRiseSet:
    def __init__(self, year, month, day, longitude):
        self.year = year
        self.month = month
        self.day = day
        self.longitude = longitude

    def calculate(self):
        baseDate = date(self.year, 1, 1)

        inputDate = date(self.year, self.month, self.day)
        daysNum = (inputDate - baseDate).days

        delta = math.radians(-23.5 * math.cos(math.radians(360/365*(daysNum+10))))
        theta = math.radians(37.5)
        a = math.radians(-0.83)

        w = math.acos((math.sin(a) - (math.sin(delta) * math.sin(theta))) / (math.cos(delta) * math.cos(theta)))
        w = math.degrees(w)

        longitudeDiff = int((135-self.longitude)/15*60)

        setHour = int(w // 15) + 12
        setMinute = round(w % 15 / 15 * 60)
        setTime = dt.timedelta(hours=setHour, minutes=setMinute) + dt.timedelta(minutes=longitudeDiff)

        riseHour = int(24 - (setHour+setMinute/60))
        riseMinute = round((24 - (setHour+setMinute/60) - riseHour)*60)
        riseTime = dt.timedelta(hours=riseHour, minutes=riseMinute) + dt.timedelta(minutes=longitudeDiff)

        return str(riseTime), str(setTime)