from io import BytesIO
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import requests


def print_usage():
    print("Usage:")
    print("--handle [user handle] – directly enter the handle of the user whose data you want to get")
    print("--no-gui – print the user data to terminal instead of creating a GUI to show them")


# try getting user from codeforces api
def get_user(user_handle):
    request = requests.get("https://codeforces.com/api/user.info", {"handles": user_handle})
    return request.json()


# extract some of the values
def extract_values(user_data):
    value_keys = ["rating", "maxRating", "rank", "maxRank"]
    values = []
    for key in value_keys:
        try:
            values.append(user_data[key])
        except KeyError:
            values.append("unknown")

    return tuple(values)


# show data about the user with Tkinter
def show_user_data(handle):
    if handle == "":
        messagebox.showerror("Error", "Enter users handle")
    else:
        user = get_user(handle)
        if user['status'] == "OK":
            user_data = user['result'][0]

            profile_picture_url = "https:%s" % user_data['avatar']
            profile_picture_data = requests.get(profile_picture_url).content
            profile_picture_pil = Image.open(BytesIO(profile_picture_data))
            profile_picture_height = int(
                float(profile_picture_pil.size[1]) *
                float(80 / float(profile_picture_pil.size[0])))
            profile_picture_pil = profile_picture_pil.resize((80, profile_picture_height), Image.ANTIALIAS)

            values = extract_values(user_data)

            user_profile_window = Tk()
            user_profile_window.title("Codeforces %s" % handle)
            user_profile_window.geometry("300x%d" % int(95 + profile_picture_height))

            profile_picture_canvas = Canvas(user_profile_window, height=str(profile_picture_height), width="80")
            profile_picture_canvas.grid(column=0, row=0, sticky="w")
            profile_picture = ImageTk.PhotoImage(profile_picture_pil, master=profile_picture_canvas)
            profile_picture_canvas.create_image(0, 0, image=profile_picture, anchor="nw")
            title_label = Label(user_profile_window, text=handle, font="Arial 20 bold")
            title_label.grid(column=1, row=0, sticky="w")

            rating_label = Label(user_profile_window, text="current rating: ", font="Arial 11 bold")
            rating_label.grid(column=0, row=1, sticky="w")
            rating_value = Label(user_profile_window, text=values[0])
            rating_value.grid(column=1, row=1, sticky="w")

            max_rating_label = Label(user_profile_window, text="highest rating: ", font="Arial 11 bold")
            max_rating_label.grid(column=0, row=2, sticky="w")
            max_rating_value = Label(user_profile_window, text=values[1])
            max_rating_value.grid(column=1, row=2, sticky="w")

            rank_label = Label(user_profile_window, text="current rank: ", font="Arial 11 bold")
            rank_label.grid(column=0, row=3, sticky="w")
            rank_value = Label(user_profile_window, text=values[2])
            rank_value.grid(column=1, row=3, sticky="w")

            max_rank_label = Label(user_profile_window, text="highest rank: ", font="Arial 11 bold")
            max_rank_label.grid(column=0, row=4, sticky="w")
            max_rank_value = Label(user_profile_window, text=values[3])
            max_rank_value.grid(column=1, row=4, sticky="w")

            user_profile_window.mainloop()
        else:
            messagebox.showerror("Error", user['comment'])


# print data about the user
def print_user_data(handle):
    user = get_user(handle)
    if user['status'] == "OK":
        user_data = user['result'][0]
        print("handle: %s" % handle)
        print(("current rating: %s\n"
               "highest rating: %s\n"
               "current rank: %s\n"
               "highest rank: %s" % extract_values(user_data)))
        exit()
    else:
        print("Error: %s" % user['comment'])
        exit(1)


def main():
    handle_from_args = ""

    # --help
    if "--help" in sys.argv:
        print_usage()
        exit()

    # --handle [user handle]
    if "--handle" in sys.argv:
        try:
            handle_from_args = sys.argv[sys.argv.index("--handle") + 1]
        except IndexError:
            print_usage()
            exit(1)

    # --no-gui
    if "--no-gui" in sys.argv:
        if handle_from_args == "":
            handle_from_args = input("Enter the handle of the user whose data you want to get: ")
        print_user_data(handle_from_args)
    # gui
    else:
        if handle_from_args == "":
            user_lookup_window = Tk()
            user_lookup_window.title("Codeforces Lookup")
            user_lookup_window.geometry("250x85")

            user_handle_label = Label(user_lookup_window, text="Enter users handle:")
            user_handle_label.pack()

            user_handle_input = Entry(user_lookup_window, width=28)
            user_handle_input.pack()

            user_handle_submit = Button(user_lookup_window, text="Show profile",
                                        command=lambda: show_user_data(user_handle_input.get()))
            user_handle_submit.pack(pady=(5, 0))

            user_lookup_window.mainloop()
        else:
            show_user_data(handle_from_args)


if __name__ == '__main__':
    main()
