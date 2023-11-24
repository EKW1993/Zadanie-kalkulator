import logging

logging.basicConfig(level=logging.INFO)

def dodawanie(numbers):
    result = sum(numbers)
    return result

def odejmowanie(numbers):
    result = numbers[0]
    for i in range(1, len(numbers)):
        result -= numbers[i]
    return result

def mnozenie(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

def dzielenie(numbers):
    result = numbers[0]
    for i in range(1, len(numbers)):
        result /= numbers[i]
    return result

def main():
    print("Podaj działanie, posługując się odpowiednią liczbą:")
    print("1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie")

    typ_dzialania = int(input())

    if typ_dzialania not in [1, 2, 3, 4]:
        print("Nieprawidłowy wybór.")
        return

    print("Podaj numer 1:")
    number1 = float(input())
    print("Podaj numer 2:")
    number2 = float(input())

    logging.info(f"Wybrane działanie: {typ_dzialania}")
    logging.info(f"Argumenty: {number1}, {number2}")

    if typ_dzialania == 1:
        result = dodawanie([number1, number2])
        print(f"Dodaję {number1} i {number2}")
    elif typ_dzialania == 2:
        result = odejmowanie([number1, number2])
        print(f"Odejmuję {number2} od {number1}")
    elif typ_dzialania == 3:
        result = mnozenie([number1, number2])
        print(f"Mnożę {number1} i {number2}")
    else:
        result = dzielenie([number1, number2])
        print(f"Dzielę {number1} przez {number2}")

    print(f"Wynik to {result}")

if __name__ == "__main__":
    main()