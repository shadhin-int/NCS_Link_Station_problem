import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x},{self.y}"

    def get_distance_to(self, other):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)


class Device(Point):

    def best_link_station_with_power(self, best_station, power):
        if power:
            return f"Best link station for point {self} is " + \
                f"{best_station} with power {power}\n"
        return f"No link station within reach for point {self}\n"

    def get_best_link_station_with_power(self, link_stations):
        best_power = 0
        best_station = link_stations[0]
        for station in link_stations:
            power = station.get_power(self)
            if power > best_power:
                best_station = station
                best_power = power
        return self.best_link_station_with_power(best_station, best_power)


class LinkStation(Point):

    def get_power(self, point):
        distance = self.get_distance_to(point)
        return (self.reach - distance)**2 if distance < self.reach else 0

    def __init__(self, x, y, reach):
        Point.__init__(self, x, y)
        self.reach = reach


def run_for_default_data():
    """Run program with the given data"""
    # initialize data
    link_stations = [
        LinkStation(0, 0, 10),
        LinkStation(20, 20, 5),
        LinkStation(10, 0, 12)
    ]
    devices = [
        Device(0, 0),
        Device(100, 100),
        Device(15, 10),
        Device(18, 18)
    ]

    results = ""
    # calculate best link stations and get the results
    for device in devices:
        results += device.get_best_link_station_with_power(link_stations)

    return results


if __name__ == "__main__":
    print(run_for_default_data())
