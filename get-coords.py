import csv
from geopy.geocoders import Nominatim


def get_geoinfo(fulladdr):
    geolocator = Nominatim(user_agent="philnc-test")
    location = geolocator.geocode(fulladdr)
    return(location)


with open('locations.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            fulladdr = row[1] + "," + row[2] + "," + row[3] + " " + row[4] \
                + " " + row[5]
            print(f'Input address: {fulladdr}')
            location = get_geoinfo(fulladdr)
            print(location.address)
            print((location.latitude, location.longitude))
            print('\n')
