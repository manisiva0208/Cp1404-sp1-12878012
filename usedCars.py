"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac7.car import Car


def main():
    """Demo test code to show how to use car class."""
    bus = Car(180, "bus")
    bus.drive(30)
    print("fuel =", bus.fuel)
    print("odo =", bus.odometer)
    print(bus)

    limo = Car(100, "limo")
    limo.add_fuel(20)
    print("limo fuel =", limo.fuel)
    limo.drive(115)
    print("limo odo =", limo.odometer)
    print(limo)
main()
