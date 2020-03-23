from lib import *

if __name__ == '__main__':
    names_range = get_names(names_list, 100)
    print(get_names(names_list, 100))
    print(get_name_most_often(names_range))
    print(get_rarely_letter(names_range))
    print(get_latest_log('log'))