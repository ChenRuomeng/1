import csv
import operator
file_opener = open("songs.csv")
file_reader = csv.reader(file_opener)
file_writer = open("songs.csv", "a")
sorted_data = sorted(file_reader, key=operator.itemgetter(1))


def main():
    menu = """
    Menu:
    L - List songs
    A - Add new song
    C - Complete a song
    Q - Quit
    """
    count = 0
    for i in sorted_data:
        count += 1
    print("Songs To Learn 1.0 - by Chen Ruomeng \n{} songs loaded from songs.csv".format(count))

    while True:
        print(menu)
        menu_code = str(input(">>>")).upper()
        if menu_code == "L":
            list_songs()
        elif menu_code == "A":
            add_new_song()
        elif menu_code == "C":
            complete_a_songs()
        elif menu_code == "Q":
            quit()
            break
        else:
            print("Invalid menu choice")
    print("Have a nice day :)")

def list_songs():
    count = 0
    count1 = 0
    count2 = 0
    print("Songs List:")
    for line in sorted_data:
        count += 1
        if "y" in line[3]:
            count1 += 1
            print("{}.* {:40} -\t{:40}({})".format(count, line[0], line[1], line[2], line[3]))
        else:
            count2 += 1
            print("{}.  {:40} -\t{:40}({})".format(count, line[0], line[1], line[2], line[3]))
    print("{} songs learned, {} songs still to learn".format(str(count2),str(count1)))
def complete_a_songs():
    print("Songs List:")
    count = -1
    count1 = -1
    for line in sorted_data:
        count += 1
        if "y" in line[3]:
            print("{}.* {:40} -\t{:40}({})".format(count, line[0], line[1], line[2], line[3]))
        else:
            print("{}.  {:40} -\t{:40}({})".format(count, line[0], line[1], line[2], line[3]))

    while True:
        try:
            user_input = int(input("Enter the number of a song to mark as completed \n>>>"))
        except ValueError:
            print("Invalid input; enter a valid number:")
        else:
            if count >= user_input >= 0:
                for line2 in sorted_data:
                    if "y" in line2[3]:
                        count1 += 1
                        if count1 == user_input:
                            file_writer2 = open("songs.csv", "w")
                            file_writer2.writelines(line2[0] + "," + line2[1] + "," + line2[2] + "," + "n")
                            print("{} by {} marked as completed".format(line2[0], line2[1]))
                            file_writer2.close()
                        else:
                            file_writer.writelines("\n" + line2[0] + "," + line2[1] + "," + line2[2] + "," + line2[3])
                    else:
                        file_writer.writelines("\n" + line2[0] + "," + line2[1] + "," + line2[2] + "," + line2[3])
                break
            else:
                print("Invalid input")
                break

def add_new_song():
    title = input("Title:")
    while title == "":
        print("Input can not be blank")
        title = input("Title:")
    artist = input("Artist:")
    while artist =="":
        print("Input can not be blank")
        artist = input("Artist:")
    while True :

        try:
            year = int(input("Year:"))
        except ValueError:
            print("Invalid input; enter a valid number")
        else:
            if year <= 0:
                print("Number must be >= 0")
            else:
                break
        file_writer.write("\n" + title + "," + artist + "," + str(year) + "," + "r")
    print("{} by {}, ({}) added to songs list".format(title, artist, year))

def quit():
    count = 0
    for i in sorted_data:
        count += 1
    print("{} songs saved to songs.csv".format(count))
    file_opener.close()
    file_writer.close()
main()