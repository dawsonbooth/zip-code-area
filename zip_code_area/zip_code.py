from __future__ import annotations

import geopy.distance


class ZIPCode:
    __slots__ = 'zip_code', 'city', 'state', 'latitude', 'longitude', 'classification', 'population'
    zip_code: str
    city: str
    state: str
    latitude: float
    longitude: float
    classification: str
    population: int

    def __init__(self, zip_code: str, city: str, state: str, latitude: float, longitude: float, classification: str, population: int):
        self.zip_code = zip_code
        self.city = city
        self.state = state
        self.latitude = latitude
        self.longitude = longitude
        self.classification = classification
        self.population = population

    def __repr__(self):
        return self.zip_code

    def __str__(self):
        return self.zip_code

    def distance(self, other: ZIPCode) -> float:
        return geopy.distance.GeodesicDistance(
            (self.latitude, self.longitude),
            (other.latitude, other.longitude)
        ).miles
