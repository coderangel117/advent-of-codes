def get_file_content(file_path):
    with open(file_path, "r") as file:
        return file.read()


def define_list():
    file = get_file_content("input.txt").split()
    left_list = []
    right_list = []

    for i in range(len(file)):
        if i % 2 == 0:
            left_list.append(file[i])
        else:
            right_list.append(file[i])

    return left_list, right_list


def get_differences_from_lists(a, b):
    difference = 0
    a, b = define_list()
    a.sort()
    b.sort()
    for i in range(len(a)):
        difference += abs(int(a[i]) - int(b[i]))
    print(difference)


def get_similarities_from_lists(a, b):
    similarity = 0
    a, b = define_list()
    for i in range(len(a)):
        similarity += int(a[i]) * b.count(a[i])
    print(similarity)


def main():
    a, b = define_list()
    # get_differences_from_lists(a, b)
    get_similarities_from_lists(a, b)


if __name__ == "__main__":
    main()
