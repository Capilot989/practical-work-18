import json


def list_sort(json_data: str) -> list[list[str, int]]:
        list_data = json.loads(json_data)
        sorted_list = sorted(
                list_data, key=lambda x: x[1], reverse=True
        )
        return sorted_list


if __name__ == "__main__":
        data = ('[["adc", 5], ["dwa", 3], ["wab", 1],'
                ' ["ded", 15], ["pda", 3], ["dee", 7]]')
        print(list_sort(data))
