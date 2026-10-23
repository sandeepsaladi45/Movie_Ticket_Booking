class User:
    def __init__(self, name, phone, email, is_admin):
        self.name = name 
        self.phone = phone
        self.email = email
        self.is_admin = is_admin

    def user_details(self):
        return f"{self.name}, {self.phone}, {self.email}, {self.is_admin}\n"

class Auth:
    def register(self):
        name = input("Enter your Name: ")
        phone = int(input("Enter your Phone number: "))
        email = input("Enter your Email: ")
        is_admin =input("if your an admin enter Yes else No: ")
        new_user = User(name, phone, email, is_admin)

        with open("Users.txt", "r") as file:
            lines = file.readlines()

        is_found = False
        for line in lines:
            details = line.strip().split(", ")
            if details[0] == name:
                is_found = True
                break
        if is_found:
            print(f"User with {name} is already exists!")
        else:
            with open("Users.txt", "a") as file:
                file.write(new_user.user_details())

    def login(self):
        name = input("Enter your name: ")
        email = input("Enter your Email: ")

        with open("Users.txt", "r") as file:
            lines = file.readlines()

        is_found = False
        for line in lines:
            details = line.strip().split(", ")
            if details[0] == name and details[2] == email:
                is_found = True
                break

        if is_found:
            print(f"Login Successfull")
        else:
            print("User doesn't exists!")

class Movies_List:
    def __init__(self, moviename, price,show_timings, seats):
        self.moviename = moviename
        self.price = price
        self.show_timings = show_timings
        # self.showtime = showtime
        self.seats = seats

    def booking_details(self):
        return f"{self.moviename}, {self.price}, {self.show_timings}, {self.seats}\n"

class Movies:
    def add_movies(self):
        moviename = input("Enter the Movie name: ")
        price = int(input("Enter the price of the Ticket: "))
        show_timings = input("Enter the shows: ").split()
        seats = input("Enter no of Seats: ")
        list = Movies_List(moviename, price, show_timings, seats)

        with open("Movies.txt", "r") as file:
            movies = file.readlines()

        is_found = False
        for movie in movies:
            item = movie.strip().split(",")
            if item[0] == moviename:
                is_found = True
                break
        else:
            with open("Movies.txt", "a") as file:
                file.write(list.booking_details())

    def view_movies(self):
        with open("Movies.txt", "r") as file:
            movies = file.readlines()
            print(f"|MovieName||Price||Show-timings||seats")
            print("--------------------------------")
            for movie in movies:
                details = movie.strip()
                print(details)

    def remove_movie(self):
        moviename = input("Enter the name of Movie: ")

        with open("Movies.txt","r") as file:
            movies = file.readlines()

        is_found = False
        for movie in movies:
            details = movie.strip().split(",")
            if details[0] == moviename:
                is_found = True
                break
        if is_found:
            with open("Movies.txt", "w") as file:
                for movie in movies:
                    item = movie.strip().split(",")
                    if item[0]!=moviename:
                        file.write(movie)
        else:
            print(f"Name with {moviename} is not found")

class Ticket_Booking(Movies):
    def __init__(self, User_name):
        self.User_name = User_name

    def view_movieslist(self): 
        cinema = Movies()
        cinema.view_movies()

    def book_ticket(self):
        name = input("Enter your name: ")
        moviename = input("Enter the movie name: ")
        seats = input("Enter no of seats: ")

        with open("Movies.txt", "r") as file:
            movies = file.readlines()

        is_found = False
        updated = None
        with open("Movies.txt","r") as file:

            for movie in movies:
                details = movie.strip().split(",")
                if details[0] == moviename:
                    is_found = True
                    updated = details
                    q =int(details[-3]) - 1
                    file.write(f"{details[0]}, {details[1]}, {q}")
                else:
                    file.write(movies)

            if is_found:
                with open("Cart.txt", "r") as file:
                    movies = file.readlines()
                is_found = False
                with open("Cart.txt", "w") as file:
                    for movie in movies:
                        details = movie.strip().split(",")
                        if details[0] == moviename and details[3] == seats:
                            is_found = True
                            q = int(details[-3]) + 1
                            file.write(f"{details[0]}, {details[1]}, {q}")
                        else:
                            file.write(movie)
            else:
                print("Movie tickets Sold-Out")
        




                            
# def admin():
#     while True:
#         print("1. To add Movies")
#         print("2. To View Movies")
#         print("3. To Remove Movies")
#         print("4. Log-out")
#         ch = input("Enter your Choice: ")
#         m = Movies()
#         if ch == 1:
#             m.add_movies()
#         elif ch == 2:
#             m.view_movies()
#         elif ch == 3:
#             m.remove_movie()
#         elif ch == 4:
#             print("Logged_out Successfully")
#             break
#         else:
#             print("Enter a valid option")

# def Customer():
#     while True:
#         print("1. Movies")
#         print("2. Book a Movie")
#         print("3.View Booking")
#         print("3. Cancel Booking")
        
                


bt = Ticket_Booking()
# bt.view_movieslist()         
bt.book_ticket()



m = Movies()
# m.add_movies()
# m.view_movies()
# m.remove_movie()


# auth = Auth()
# auth.register()
# auth.login()