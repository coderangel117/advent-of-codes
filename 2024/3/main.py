import re


def get_file_content(file_path):
    with open(file_path, "r") as file:
        return file.read()


def mul(a, b):
    return a * b


def search_multiplier_valid():
    regex = r"mul\((\d+),(\d+)\)"
    test_str = get_file_content("input.txt")
    # test_str = "mul(8,8)xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

    matches = re.finditer(regex, test_str, re.MULTILINE)
    result = 0
    for matchNum, match in enumerate(matches, start=1):
        result += mul(int(match.group(1)), int(match.group(2)))
    print(result)


def main():
    search_multiplier_valid()


if __name__ == "__main__":
    main()
