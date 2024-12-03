def get_file_content(file_path):
    with open(file_path, "r") as file:
        return file.read()


def define_list():
    file = get_file_content("test.txt").split("\n")
    for i in range(len(file) - 1):
        line = file[i].split(" ")
        print(line)
        for j in range(len(line)):
            level = int(line[j])
            # verify that adjacent numbers is decreasing max to 3
            if j < len(line):
                if level + level + 1 <= 3:
                    print("foo", level - level + 1)
                    print("yes - ", level)
                if level - level + 1 < 3:
                    print("yes + ", level)
                if level == level + 1:
                    break


def main():
    define_list()


if __name__ == "__main__":
    main()
