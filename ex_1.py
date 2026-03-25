def count_upper(*, text: str, i: int, j: int) -> int:
    """
        Count the number of uppercase letters in a substring of the given text.

        This function extracts a substring from position i to j (1-indexed, inclusive)
        and counts how many characters in that substring are uppercase letters.

        Args:
            text: The input string to process
            i: Starting position (1-indexed, inclusive)
            j: Ending position (1-indexed, inclusive)

        Returns:
            The number of uppercase letters in the specified substring
        """
    procceced_string = text[i-1:j]
    count = len(
        list(filter(lambda el: el.isupper(), procceced_string))
    )
    return count


if __name__ == "__main__":
    text = input("Enter the text ")
    i = int(input("Enter the start number: "))
    j = int(input("Enter the end number: "))
    print(count_upper(text=text, i=i, j=j))
