import json


def list_sort(json_data: str) -> list[list[str, int]]:
    """
    Sort a JSON array of sublists by the second element in descending order.

    This function takes a JSON string representing a list of sublists,
    where each sublist contains a string and an integer. It parses the JSON
    and sorts the sublists based on the integer value in descending order.

    Args:
        json_data: JSON string containing a list of [string, int] pairs

    Returns:
        Sorted list of [string, int] pairs, sorted by the integer value
        in descending order (highest to lowest)
    """
        list_data = json.loads(json_data)
        sorted_list = sorted(
                list_data, key=lambda x: x[1], reverse=True
        )
        return sorted_list


if __name__ == "__main__":
        data = ('[["adc", 5], ["dwa", 3], ["wab", 1],'
                ' ["ded", 15], ["pda", 3], ["dee", 7]]')
        print(list_sort(data))
