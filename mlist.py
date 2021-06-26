from switch import Switch


class MList:
    mlist = [None]

    # z parametrem określającym pojemność listy
    # (liczbę elementów jaką maksymalnie może przechować)
    def __init__(self):
        self.mlist = []
        self.capacity = 10

    def start(self):
        try:
            cap = int(input("Please enter the desired max capacity: \n"))
            self.capacity = cap
            if (cap == 69):
                print("Nice.\n")
        except ValueError:
            print("You can't even do as much? Give it back. It's set to 10.\n")

    # wypisuje informacje o liście, w tym jej aktualny rozmiar,
    # pojemność oraz przechowywane elementy;
    def write_out(self):
        print("List's elements: " + str(self.mlist) +
              ",\nCurrent size: [" + str(len(self.mlist)) +
              "],\nCapacity: [" + str(self.capacity) + "]\n")

    # dodaje element x do
    # listy pod warunkiem, że nie zostanie przekroczona
    # jej pojemność; gdy element zostanie dodany funkcja
    # powinna zwrócić True, w przeciwnym wypadku False
    def add_element(self):
        if (len(self.mlist) < self.capacity):
            uinput = input("Insert the new record: ")
            if (uinput == 69):
                print("Nice.\n")
            self.mlist.append(uinput)
            print("New record added.\n")
            return True
        else:
            print("Sorry, there's no space left in the list.\n")
            return False

    def find_record(self):
        try:
            record = self.mlist.index(input("Enter the record you'd"
                                            " like to find: "))
            print("The record You've been looking for has index "
                  + str(record + 1) + ".\n")
        except ValueError:
            print("Value not found in the list.\n")

    def get_element(self):
        element_index = int(input("Enter the index you'd like to check:")) - 1
        try:
            print("The element under this index is: "
                  + str(self.mlist[int(element_index)]) + ".\n")
        except IndexError:
            print("Value not in the scope of this list.\n")
        except ValueError:
            print("Incorrect input value.\n")

    # zwracającą aktualną liczbę elementów
    def return_size(self):
        print("The size of the list, sir: " + str(len(self.mlist)) + ".\n")

    # zwracającą aktualną pojemność listy,
    def return_max_size(self):
        print("The capacity of the list, sir: " + str(self.capacity) + ".\n")

    # która usuwa wszystkie powtórzenia danego elementu na liście, tzn.
    # po jej wykonaniu na liście powinien być tylko pierwszy w kolejności
    # element x
    def del_repeating(self):
        count = 0
        i = 0
        value = input("Enter the value of which duplicates"
                      " you want to remove:\n")
        while (i <= len(self.mlist)):
            if (value == self.mlist[i]):
                count += 1
                if (count > 1):
                    del self.mlist[i]
                    i += 1
                else:
                    i += 1
            else:
                i += 1

    # która odwraca kolejność przechowywanych elementów (2, 6, 4 -> 4, 6, 2)
    def reverse_order(self):
        self.mlist.reverse()

    # zwiększającą pojemność listy o x. Funkcja powinna zwracać
    # True, gdy udało się zwiększyć pojemność; False gdy pojemności
    # nie udało się zwiększyć (np. nie zwiększamy pojemności, gdy
    # liczba x jest mniejsza od 0, nie zmniejszamy pojemności do
    # liczby mniejszej niż liczba elementów w liście)
    def expand_list(self):
        x = input("Get me this sweet x number Cortana: ")
        try:
            if (int(x) < self.capacity and int(x) < 0):
                print("That's a no chief.\n")
            else:
                self.capacity = self.capacity + int(x)
                self.mlist.extend(x)
                print("Extended with " + str(x) + " new records.\n")
        except ValueError:
            print(
                "OOPSIE WOOPSIE!! Uwu We made a fucky wucky!! A wittle "
                "fucko boingo! The code monkeys at our headquarters are "
                "working VEWY HAWD to fix this! (Value Error - get out "
                "of here)\n")
            print("You're getting [-1].\n")

    def size_down(self):
        x = int(input("Get me this sweet x number Cortana: "))
        try:
            if (x > self.capacity):
                print("That's a no chief.\n")
            else:
                self.capacity = self.capacity - x
                del self.mlist[(self.capacity - x): self.capacity]
                print("Sized down the list by " + str(x) + " records.\n")
        except ValueError:
            print(
                "OOPSIE WOOPSIE!! Uwu We made a fucky wucky!! A wittle "
                "fucko boingo! The code monkeys at our headquarters are "
                "working VEWY HAWD to fix this! (Value Error - get out "
                "of here)\n")
            print("You're getting [-1].\n")

    def menu(self):
        while True:
            action = input("Tell me what would you like to do:\n"
                           "|| write out "
                           "|| add element "
                           "|| find record "
                           "|| get element "
                           "|| return size "
                           "|| return capacity "
                           "|| delete repeating "
                           "|| reverse "
                           "|| expand list "
                           "|| size down "
                           "|| exit ||\n")
            with Switch(action) as case:
                if case('write out'):
                    self.write_out()
                if case('add element'):
                    self.add_element()
                if case('find record'):
                    self.find_record()
                if case('get element'):
                    self.get_element()
                if case('return size'):
                    self.return_size()
                if case('return capacity'):
                    self.return_max_size()
                if case('delete repeating'):
                    self.del_repeating()
                if case('reverse'):
                    self.reverse_order()
                if case('expand list'):
                    self.expand_list()
                if case('size down'):
                    self.size_down()
                if case('exit'):
                    break
                if case.default:
                    print("Unknown command woopsie x3\n")
