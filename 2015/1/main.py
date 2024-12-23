def get_file_content(file_path):
    with open(file_path, "r") as file:
        return file.read()


def define_floor():
    floor = 0
    file = get_file_content("input.txt")
    for i in range(len(file)):
        if file[i] == "(":
            floor += 1
        elif file[i] == ")":
            floor -= 1
        if floor == -1:
            print(i + 1)
            break
    print(floor)


def main():
    define_floor()


if __name__ == "__main__":
    main()
