import re
from datetime import datetime


def couting_information(_object):
    if _object:
        now_time = str(datetime.now())[11:16].split(':')
        last_time = re.split(':|-', _object.last().time)
        now_min = int(now_time[0]) * 60 + int(now_time[1])
        last_min = int(last_time[0]) * 60 + int(last_time[1]) if int(last_time[0]) <= int(now_time[0]) else int(last_time[0]) * 60 + int(last_time[1]) - 1440
        time_to_eat = [(now_min - last_min) // 60, (now_min - last_min) % 60]
        last_min_anticipated = int(last_time[0]) * 60 + int(last_time[1])
        time_anticipated_min = last_min_anticipated + 180 if last_min_anticipated + 180 <= 1440 else last_min_anticipated + 180 - 1440
        time_anticipated = [time_anticipated_min // 60, time_anticipated_min % 60]
        hours_time = str(time_to_eat[0]).zfill(2)
        min_time = str(time_to_eat[1]).zfill(2)
        hours_time_anticipated = str(time_anticipated[0]).zfill(2)
        min_time_anticipated = str(time_anticipated[1]).zfill(2)
    else:
        hours_time = '--'
        min_time = '--'
        hours_time_anticipated = '--'
        min_time_anticipated = '--'

    return hours_time, min_time, hours_time_anticipated, min_time_anticipated
