"""Exploration of gpxpy module.

References:
    http://www.topografix.com/gpx_manual.asp
"""

import os
import math

import gpxpy
import pytz
import matplotlib.pyplot as pyplot


DATA_PATH = 'data'
GPX_FILE = '20170521.gpx'
TITLE = 'Mount Washington - Sunday May 21th'
TIMEZONE = 'US/Eastern'


def main():
    """Main!"""
    filename = os.path.splitext(GPX_FILE)[0]

    # Read GPX file
    with open(os.path.join(DATA_PATH, GPX_FILE), 'r') as fid:
        gpx = gpxpy.parse(fid)

    # Write XML conversion file
    xml = gpx.to_xml()
    with open(os.path.join(DATA_PATH, filename+'.xml'), 'w') as fid:
        fid.writelines(xml)

    # Retrieve hours and elevation
    timezone = pytz.timezone(TIMEZONE)
    all_hours = []
    all_elevation = []
    for point in gpx.tracks[0].segments[0].points:
        all_elevation.append(point.elevation)
        utc_dt = pytz.utc.localize(point.time)
        my_tz_dt = timezone.normalize(utc_dt.astimezone(timezone))
        frac_hour = my_tz_dt.hour + my_tz_dt.minute/60 + my_tz_dt.second/3600
        all_hours.append(frac_hour)

    # Plot elevation vs seconds
    pyplot.plot(all_hours, all_elevation)
    pyplot.xticks(range(math.floor(all_hours[0]), math.ceil(all_hours[-1]), 1))
    pyplot.xlabel('time (h)')
    pyplot.ylabel('elevation (m)')
    pyplot.title(TITLE)
    pyplot.grid(True)
    pyplot.savefig(os.path.join(DATA_PATH, filename+'_elevation.png'))
    pyplot.show()


if __name__ == '__main__':
    main()
