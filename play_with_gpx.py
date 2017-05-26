"""Exploration of gpxpy module.

References:
    http://www.topografix.com/gpx_manual.asp
"""

import os

import gpxpy
import matplotlib.pyplot as pyplot


DATA_PATH = 'data'
GPX_FILE = r'20170521.gpx'


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
    # Plot elevation vs seconds
    all_seconds = []
    all_elevation = []
    start_time = gpx.tracks[0].segments[0].points[0].time
    for point in gpx.tracks[0].segments[0].points:
        all_elevation.append(point.elevation)
        nb_seconds = (point.time - start_time).seconds
        all_seconds.append(nb_seconds)
    pyplot.plot(all_seconds, all_elevation)
    pyplot.xlabel('time (s)')
    pyplot.ylabel('elevation (m)')
    pyplot.title('Mount Washington - Sunday May 21th')
    pyplot.grid(True)
    pyplot.savefig(os.path.join(DATA_PATH, filename+'_elevation.png'))
    pyplot.show()


if __name__ == '__main__':
    main()
