# from data in test.txt
#   7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
#   1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
#   9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
#   1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
#   8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
#   1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.

# PART 2

#   7 6 4 2 1: Safe without removing any level.
#   1 2 7 8 9: Unsafe regardless of which level is removed.
#   9 7 6 2 1: Unsafe regardless of which level is removed.
#   1 3 2 4 5: Safe by removing the second level, 3.
#   8 6 4 4 1: Safe by removing the third level, 4.
#   1 3 6 7 9: Safe without removing any level.


def get_file_content(file_path):
    with open(file_path, "r") as file:
        return file.read()


def define_safe_list():
    file = get_file_content("input.txt").split("\n")  # Become table of string
    safe_list = 0
    for i in range(len(file) - 1):
        line = file[i].split(" ")
        differences = [int(line[i + 1]) - int(line[i]) for i in range(len(line) - 1)]
        sums = [int(line[i]) - int(line[i + 1]) for i in range(len(line) - 1)]
        if all(difference in [1, 2, 3] for difference in differences):
            safe_list += 1
        elif all(sum in [1, 2, 3] for sum in sums):
            safe_list += 1
        else:
            for j in range(len(line)):
                new_line = line.copy()
                new_line.pop(j)
                differences = [
                    int(new_line[i + 1]) - int(new_line[i])
                    for i in range(len(new_line) - 1)
                ]
                sums = [
                    int(new_line[i]) - int(new_line[i + 1])
                    for i in range(len(new_line) - 1)
                ]
                if all(difference in [1, 2, 3] for difference in differences):
                    safe_list += 1
                    break
                elif all(sum in [1, 2, 3] for sum in sums):
                    safe_list += 1
                    break

    print(safe_list)


def main():
    define_safe_list()


if __name__ == "__main__":
    main()
