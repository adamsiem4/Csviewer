import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def load_csv(file_path):
    
    try:
        data = pd.read_csv(file_path).head(100)  # Limit to the first 100 rows
        return data
    except Exception as e:
        messagebox.showerror("Error", f"Error loading file: {e}")
        return None

def display_data(data, tree):
    """Display the DataFrame in the Treeview widget."""
    # Clear existing data in the Treeview
    tree.delete(*tree.get_children())

    # Add new data to the Treeview
    tree["columns"] = list(data.columns)
    tree["show"] = "headings"

    for col in data.columns:
        tree.heading(col, text=col)
        tree.column(col, width=120, anchor="center")

    for index, row in data.iterrows():
        tree.insert("", "end", values=list(row))

def sort_data(data, tree, sort_column, ascending):
    """Sort the DataFrame and update the Treeview."""
    try:
        sorted_data = data.sort_values(by=sort_column, ascending=ascending)
        display_data(sorted_data, tree)
    except Exception as e:
        messagebox.showerror("Error", f"Error sorting data: {e}")

def filter_data(data, tree):
    """Filter the DataFrame based on user input and update the Treeview."""
    filter_window = tk.Toplevel()
    filter_window.title("Filter Data")
    filter_window.configure(bg="#2E2E2E")

    tk.Label(filter_window, text="Select column to filter by:", fg="white", bg="#2E2E2E").pack(pady=5)
    filter_column = tk.StringVar()
    filter_column.set(data.columns[0])

    column_menu = ttk.OptionMenu(filter_window, filter_column, *data.columns)
    column_menu.pack(pady=5)

    tk.Label(filter_window, text="Enter value to filter:", fg="white", bg="#2E2E2E").pack(pady=5)
    filter_value = tk.Entry(filter_window)
    filter_value.pack(pady=5)

    def apply_filter():
        value = filter_value.get()
        column = filter_column.get()
        try:
            filtered_data = data[data[column].astype(str).str.contains(value, case=False, na=False)]
            display_data(filtered_data, tree)
            filter_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Error filtering data: {e}")

    tk.Button(filter_window, text="Apply Filter", command=apply_filter, bg="#4CAF50", fg="white", activebackground="#45A049").pack(pady=10)

def main():
    # Load fixed CSV file
    file_path = './src/social_media_entertainment_data.csv'
    data = load_csv(file_path)
    if data is None:
        return

    # Create main application window
    root = tk.Tk()
    root.title("CSV Viewer and Sorter")
    root.state('zoomed')  # Open in fullscreen mode

    # Apply dark theme
    root.configure(bg="#2E2E2E")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview",
                    background="#333333",
                    foreground="white",
                    rowheight=25,
                    fieldbackground="#333333")
    style.map("Treeview",
              background=[("selected", "#4CAF50")],
              foreground=[("selected", "white")])

    frame = tk.Frame(root, bg="#2E2E2E")
    frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    # Create a Treeview widget with scrollbars
    tree = ttk.Treeview(frame, selectmode="browse")

    x_scrollbar = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
    x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

    y_scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    tree.configure(xscroll=x_scrollbar.set, yscroll=y_scrollbar.set)
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    display_data(data, tree)

    def sort_file():
        sort_window = tk.Toplevel(root)
        sort_window.title("Sort Options")
        sort_window.configure(bg="#2E2E2E")

        tk.Label(sort_window, text="Select column to sort by:", fg="white", bg="#2E2E2E").pack(pady=5)
        sort_column = tk.StringVar()
        sort_column.set(data.columns[0])

        column_menu = ttk.OptionMenu(sort_window, sort_column, *data.columns)
        column_menu.pack(pady=5)

        ascending = tk.BooleanVar(value=True)
        tk.Checkbutton(sort_window, text="Sort in ascending order", variable=ascending, bg="#2E2E2E", fg="white", selectcolor="#4CAF50").pack(pady=5)

        def apply_sort():
            sort_data(data, tree, sort_column.get(), ascending.get())
            sort_window.destroy()

        tk.Button(sort_window, text="Sort", command=apply_sort, bg="#4CAF50", fg="white", activebackground="#45A049").pack(pady=10)

    button_frame = tk.Frame(root, bg="#2E2E2E")
    button_frame.pack(pady=10)

    sort_button = tk.Button(button_frame, text="Sort Data", command=sort_file, bg="#4CAF50", fg="white", activebackground="#45A049")
    sort_button.grid(row=0, column=0, padx=5)

    filter_button = tk.Button(button_frame, text="Filter Data", command=lambda: filter_data(data, tree), bg="#2196F3", fg="white", activebackground="#1976D2")
    filter_button.grid(row=0, column=1, padx=5)

    exit_button = tk.Button(button_frame, text="Exit", command=root.quit, bg="#D32F2F", fg="white", activebackground="#B71C1C")
    exit_button.grid(row=0, column=2, padx=5)

    root.mainloop()

if __name__ == "__main__":
    main()
