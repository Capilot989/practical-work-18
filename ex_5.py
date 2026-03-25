from functools import reduce


def find_multiplication(*, a: int, b: int, c:int) -> int:
    """
    Find the product of perfect squares within a range that are multiples of c.

    This function identifies numbers in the range [a, b] that are perfect squares
    (have integer square roots) and are divisible by c, then returns their product.

    Args:
        a: Starting number of the range (inclusive)
        b: Ending number of the range (inclusive)
        c: Divisor that numbers must be divisible by

    Returns:
        The product of all perfect squares in [a, b] that are divisible by c

    Raises:
        TypeError: If no suitable numbers are found (reduce on empty sequence)
    """
    numb_list = range(a, b + 1)
    suitable_numbers = filter(
        lambda x: int(x ** 0.5) ** 2 == x and x % c == 0,
        numb_list,
    )
    result = reduce(
        lambda x, y: x * y,
        suitable_numbers
    )
    return result


if __name__ == "__main__":
    a = int(input("Enter start number: "))
    b = int(input("Enter end number: "))
    c = int(input("Enter divided number: "))
    print(find_multiplication(a=a, b=b, c=c))
