# V. Rivera Casanova

# program for semester 3 schedule
# each function takes in the time at the given day
# will include *except value errors later on


import re
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img = mpimg.imread('the_one.jpg')
imgplot = plt.imshow(img)


def mon(hr, min):
    print("Where is Vic?")

    if (hr >= 12 and min >= 10) and (hr < 15 and min >= 0):
        print("At ENGR 216")
    elif hr == 15 and min == 0:
        print("At ENGR 216")
    else:
        print("Free")


def tues_thurs(hr, min):
    print("Where am Vic?")

    if (hr >= 8 and min >= 0) and (hr < 9):
        print("At MATH 251")
    elif hr == 9 and min <= 15:
        print("At MATH 251")
    elif (hr >= 9 and min >= 35) and (hr < 10):
        print("At PHYS 206")
    elif hr == 10 and min <= 50:
        print("At PHYS 206")
    elif (hr >= 11 and min >= 0) and (hr < 15):
        print("At work")
    elif hr == 15 and min == 0:
        print("At work")
    elif (hr >= 15 and min >= 55) and (hr < 17):
        print("At CSCE 181")
    elif hr == 17 and min <= 10:
        print("At CSCE 181")
    else:
        print("Free")


def wed(hr, min):
    print("Where am Vic?")

    if (hr >= 9 and min >= 0) and (hr < 12 and min >= 0):
        print("At work")
    elif hr == 12 and min == 0:
        print("At work")
    elif (hr >= 12 and min >= 30) and (hr < 13):
        print("At PHYS 206")
    elif hr == 13 and min <= 50:
        print("At PHYS 206")
    else:
        print("Free")


def fri(hr, min):
    print("Where is Vic?")

    if (hr >= 13 and min >= 50) and (hr < 14 and min <= 40):
        print("At ENGR 216")
    elif hr == 14 and min <= 40:
        print("At ENGR 216")
    else:
        print("Free")


def sat(hr, min):
    if hr == 2 and min == 16:
        print("Where am Vic?")
        print("Probably at the hospital for alcohol poisoning.¯\_(ツ)_/¯")
        plt.show()

    else:
        print("It's the weekend bitch!")


def weekend():
    print("It's the weekend bitch!")

# makes sure hr and min are within correct range
# if not test_time() is called again with the new inputted time


def time_in_range(given_hr, given_min):
    if int(given_hr) < 0 or int(given_hr) > 23:
        print("Oops! Time input is invalid. Try again...")
        time = input("Enter specific time in xx:xx format::")
        test_time(time)

    elif int(given_min) < 0 or int(given_min) > 59:
        print("Oops! Time input is invalid. Try again...")
        time = input("Enter specific time in xx:xx format::")
        test_time(time)
    else:
        valid_nums = [given_hr, given_min]
        return valid_nums


# makes sure colon is being inputted, removes any unnecessary white spaces
# whenever the input is invalid this function is called again to recheck these conditions

def time_format(time):
    time.replace(" ", "")
    while ":" not in time:
        print("Oops! Time input is invalid. Try again...")
        time = input("Enter specific time in xx:xx format::")
    print(time)
    return time


def test_section(tm, num):
    # takes away everything except the digits and colon
    t_a = re.sub('[^\d\:]', '', tm)

    # need to fix this code so that it only accepts digits and ":"
    # while there is no more than xx:xx
    while (len(t_a) > 5) or (len(t_a) < 4):
        print("Oops! Time input is invalid. Try again pls...")
        tm = input("Enter specific time in xx:xx format:::")
        tm = time_format(tm)
        t_a = re.sub('[^\d\:]', '', tm)

    # to get hour and minute, colon is the reference

    index = t_a.find(":")
    n_hr = t_a[0:index]
    n_min = t_a[index + 1:]

    t_result = time_in_range(n_hr, n_min)

    # num is index to know which inputs already have am or pm accounted for
    # for this reason hour and minute are still in string format
    if t_a.find("0") == 0 or num == 1:
        return t_result
    else:
        hour = int(n_hr)
        if (hour >= 1) and (hour <= 12):
            d_or_n = input("Enter AM or PM::")

            if "pm" in d_or_n.lower() and hour != 12:
                hour += 12

        t_result = [str(hour), n_min]
        return t_result


def test_time(time):
    # tests so program works regardless of format the user has entered the time

    while True:
        try:
            if 'am' in time.lower():
                num = 1
                new_t = test_section(time, num)
                hour = int(new_t[0])
                minute = int(new_t[1])
                fin_time = [hour, minute]
                return fin_time

            elif 'pm' in time.lower():
                num = 1
                new_t = test_section(time, num)
                if int(new_t[0]) < 12:
                    hour = 12 + int(new_t[0])
                else:
                    hour = int(new_t[0])
                minute = int(new_t[1])
                fin_time = [hour, minute]
                return fin_time

            new_t = test_section(time, 2)

            hour = int(new_t[0])
            minute = int(new_t[1])
            fin_time = [hour, minute]
            return fin_time

        except ValueError:
            # makes sure no letters are in the input besides "am" or "pm"

            print("Oops!  That was no valid number.  Try again...")
            time = input("Enter specific time in xx:xx format::")
            time = time_format(time)

# asks user for day of the week
# asks user for specific time to search for


def main():
    hour = 0
    minute = 0

# test to make sure day is valid immediately
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    day = (input("Enter a day::")).replace(" ", "")

    while day.lower() not in days:
        print("Oops!  That was no valid day of the week.  Try again...")
        day = input("Enter a day::")

# test to check if time entered in specific format
    time1 = input("Enter specific time in xx:xx format::")
    time = time_format(time1)
# makes sure there is only 4 numbers inputted, else make you go back
    list_t = test_time(time)

# edit so however user enters time program will adjust and know
# right now still need to ask if it is am or pm
    hour = (list_t[0])
    minute = list_t[1]
    print(" ")
    print("Hour::", list_t[0])
    print("Minute::", list_t[1])


# edit if statements to be more concise
    if day == "monday":
        print("Day::", days[0])
        mon(hour, minute)
    elif day == "tuesday":
        print("Day::", days[1])
        tues_thurs(hour, minute)
    elif day == "wednesday":
        print("Day::", days[2])
        wed(hour, minute)
    elif day == "thursday":
        print("Day::", days[3])
        tues_thurs(hour, minute)
    elif day == "friday":
        print("Day::", days[4])
        fri(hour, minute)
    elif day == "saturday":
        print("Day::", days[5])
        sat(hour, minute)
    elif day == "sunday":
        print("Day::", days[6])
        weekend()


main()


# fixed hour and minute range, but will ask for am and pm twice
# not specific in the 4-5 char code, will accept 12:8' as valid
#fucntion to check that only numbers are on both sides of the ":"; can create an 'except value error'

# make more concise; try to eliminate repeating code

