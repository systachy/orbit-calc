import math

MU_EARTH = 398600.4418  # km^3/s^2
R_EARTH = 6378.137      # km


def orbital_period(altitude_km):
    r = R_EARTH + altitude_km
    return 2 * math.pi * math.sqrt(r**3 / MU_EARTH)


def orbital_velocity(altitude_km):
    r = R_EARTH + altitude_km
    return math.sqrt(MU_EARTH / r)


if __name__ == "__main__":
    altitude = float(input("Altitude above Earth (km): "))
    period = orbital_period(altitude)
    print(f"Orbital period: {period:.1f} seconds")
    print(f"Orbital velocity: {orbital_velocity(altitude):.2f} km/s")