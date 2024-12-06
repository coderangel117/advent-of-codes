# 3 858 306 too high
# 3 847 850 too high


def get_file_content(file_path):
    with open(file_path, "r") as file:
        return file.read()


def define_dimensions():
    dimension_paper = 0
    dimension_rubbon = 0
    file = get_file_content("input.txt").split("\n")
    for i in range(len(file) - 1):
        line = file[i].split("x")
        line = [int(numeric_string) for numeric_string in line]
        line.sort()
        print(line)
        l, w, h = line[0], line[1], line[2]
        print("l", l)
        print("w", w)
        print("h", h)
        dimension_paper += 2 * l * w + 2 * w * h + 2 * h * l + min(l * w, w * h, h * l)
        value = l + l + w + w
        print(value)
        value += l * w * h
        print(value)
        dimension_rubbon += l + l + w + w + (l * w * h)
    print(dimension_rubbon)


def main():
    define_dimensions()


if __name__ == "__main__":
    main()
