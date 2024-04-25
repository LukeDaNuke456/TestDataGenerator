import tkinter as tk
import createtestdata
from tkinter import ttk, messagebox

def display_vehicles():
    
    num_of_vehicles = str(entry.get())

    if not num_of_vehicles.isdigit():

        messagebox.showinfo("Alert", "Input not Valid. Enter a positive whole number.")

    else:

        vehicles = createtestdata.main(num_of_vehicles)
        clear_table()
    
        for vehicle_id, vehicle in vehicles.items():

            tree.insert("", "end", values=(vehicle_id, vehicle.year, vehicle.make, vehicle.model, vehicle.mileage, vehicle.price))

def clear_table():
    for item in tree.get_children():
        tree.delete(item)

root = tk.Tk()
root.title("Vehicle Test Data Generator GUI") 

window_width = 800
window_height = 500
root.resizable(False, False)

def center_window(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")

center_window(root, window_width, window_height)


input_frame = tk.Frame(root)
input_frame.grid(row=2, column=0, pady=10)

label = tk.Label(input_frame, text="Enter the number of vehicles you want data for:")
label.grid(row=0, column=0)

entry = tk.Entry(input_frame, width=30)  
entry.grid(row=1, column=0)

btn_create = tk.Button(input_frame, text="Create Data", command=display_vehicles)
btn_save = tk.Button(input_frame, text="Export Data (.xlsx)", command=display_vehicles)
btn_save.config(state="disabled")
btn_create.grid(row=1, column=1, padx=10)
btn_save.grid(row=1, column=2, padx=10)

columns = ("Vehicle ID", "Vehicle Year", "Vehicle Make", 
           "Vehicle Model", "Vehicle Mileage", "Vehicle Price")

style = ttk.Style()

style.theme_use("default")  # Use the default theme (can be changed)
style.configure("Custom.Treeview.Heading", background="lightblue", font=("Arial", 10, "bold"), anchor="center")
style.configure("Custom.Treeview", background="white", fieldbackground="none", rowheight=25)

tree_frame = tk.Frame(root)

tree = ttk.Treeview(tree_frame, columns=columns, show="headings", style="Custom.Treeview")

tree_height = 45  
tree['height'] = tree_height


for col in columns:
    tree.heading(col, text=col)  
    tree.column(col, width=125,  anchor="center")  

tree_frame.grid(row=3, column=0, pady=10, padx=25)
tree.grid(row=0, column=0)



root.mainloop()
