def count_numbs(*, a: int, b: int, c: int, d: int):
    """
        Count numbers in a range that satisfy specific exclusion criteria.

        This function counts numbers from a to b (inclusive) that are NOT divisible
        by c AND do NOT end with the digit d.

        Args:
            a: Starting number of the range (inclusive)
            b: Ending number of the range (inclusive)
            c: Divisor that numbers should NOT be divisible by
            d: Last digit that numbers should NOT end with

        Returns:
            The count of numbers in [a, b] that are not divisible by c and
            do not end with digit d
        """
    numb_list = range(a, b + 1)
    count = sum(
        list(map(lambda x: (x % c != 0 and x % 10 != d), numb_list))
    )
    return count


if __name__ == "__main__":
    a = int(input("Enter the start number: "))
    b = int(input("Enter the end number: "))
    c = int(input("Enter the false divider: "))
    d = int(input("Enter the digit which is not the last: "))
    print(count_numbs(a=a, b=b, c=c, d=d))
