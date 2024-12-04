# from data in test.txt
#   7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
#   1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
#   9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
#   1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
#   8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
#   1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.


def get_file_content(file_path):
    with open(file_path, "r") as file:
        return file.read()


def define_list():
    file = get_file_content("input.txt").split("\n")  # Become table of string

    safe_list = 0
    for i in range(len(file) - 1):
        line = file[i].split(" ")
        print(line)
        differences = [int(line[i + 1]) - int(line[i]) for i in range(len(line) - 1)]
        sums = [int(line[i]) - int(line[i + 1]) for i in range(len(line) - 1)]
        if all(difference in [1, 2, 3] for difference in differences):
            safe_list += 1
        elif all(sum in [1, 2, 3] for sum in sums):
            safe_list += 1
    print(safe_list)


def main():
    define_list()


if __name__ == "__main__":
    main()
