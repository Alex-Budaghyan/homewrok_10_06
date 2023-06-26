def start_with(s, prefix):
    if len(s) < len(prefix):
        return False
    for i in range(len(prefix)):
        if s[i] != prefix[i]:
            return False
    return True


def ends_with(string, suffix):
    if len(suffix) > len(string):
        return False
    return string[-len(suffix):] == suffix


def swap_strings(s1, s2):
    temp = s1
    s1 = s2
    s2 = temp
    return s1, s2


def rotate_by(arr, num):
    p = num % len(arr)
    rotated_arr = arr[-p:] + arr[:-p]
    return rotated_arr


def find_last_not_of(string, a):
    is_equal = False
    index = len(string)
    while not is_equal and index >= 0:
        is_equal = True
        index -= 1
        for i in range(len(a)):
            if string[i] == a[i]:
                is_equal = False
                break
    return string[index]


def convert_to_int(str):
    num = 0
    for i in range(len(str)):
        if not (str[i] < 48 or str[i] > 57) and str[0] == '0':
            num *= 10
            num += str[i] - 48
        elif str[0] == '0':
            raise ValueError('The string starts with 0')
        else:
            raise ValueError('The string contains not only digits')
    return num


str1 = "asdefwsa"
str2 = "asdf"
str3 = "sfdebbakn"
str4 = "akn"


print(start_with(str1, str2))
print(start_with(str3, str4))
print(ends_with(str1, str3))
print(ends_with(str3, str4))
str1, str3 = swap_strings(str1, str3)
print(str1)
print(str3)
str2, str4 = swap_strings(str2, str4)
print(str2)
print(str4)

ls = ['s', 'd', 'j', 'a']
print(find_last_not_of(str1, ls))

array = [1, 2, 3, 4, 5, 6, 7]
print(rotate_by(array, 10))

number = convert_to_int("4")
if number:
    print(number)

