def count_multiplies(*, a: int, b: int, c: int, d: int):
    """
       Calculate the sum of numbers in a range that are multiples of both c and d.

       This function generates a list of integers from a to b (inclusive) and
       returns the sum of those numbers that are divisible by both c and d.

       Args:
           a: Starting number of the range (inclusive)
           b: Ending number of the range (inclusive)
           c: First divisor
           d: Second divisor

       Returns:
           The sum of numbers in [a, b] that are divisible by both c and d
       """
    numb_list = range(a, b + 1)
    count = sum(
        list(filter(lambda x: (x % c == 0 and x % d == 0), numb_list))
    )
    return count


if __name__ == "__main__":
    a = int(input("Enter the start number: "))
    b = int(input("Enter the end number: "))
    c = int(input("Enter the first divider: "))
    d = int(input("Enter the second divider: "))
    print(count_multiplies(a=a, b=b, c=c, d=d))
