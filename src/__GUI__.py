# file: tkinter_app.py
from tkinter import *

class TkinterApp:
    def __init__(self):
        # Initialize the main window
        self.window = Tk()
        self.window.geometry("420x420")
        self.window.title("Swim Materials & Difficulty Selector")

        # Initialize shared variables
        self.material_list = []  # Stores selected swim materials
        self.difficulty = StringVar(value="None")  # Default difficulty value

        # Create and display UI components
        self.create_material_section()
        self.create_difficulty_section()
        self.create_submit_buttons()

        # Track if the user submitted data
        self.is_submitted = False

    def create_material_section(self):
        """Create checkboxes for swim materials."""
        materials_label = Label(self.window, text="Select the swim materials you have:", font=("Arial", 14))
        materials_label.pack(pady=10)

        # Variables to track checkbox states
        self.x = IntVar()
        self.y = IntVar()
        self.z = IntVar()
        self.w = IntVar()

        # Checkbuttons for swim materials
        Checkbutton(self.window, text="Kickboard", variable=self.x, onvalue=1, offvalue=0).pack(anchor="w", padx=20, pady=5)
        Checkbutton(self.window, text="Pull Buoy", variable=self.y, onvalue=1, offvalue=0).pack(anchor="w", padx=20, pady=5)
        Checkbutton(self.window, text="Fins", variable=self.z, onvalue=1, offvalue=0).pack(anchor="w", padx=20, pady=5)
        Checkbutton(self.window, text="Paddles", variable=self.w, onvalue=1, offvalue=0).pack(anchor="w", padx=20, pady=5)

    def create_difficulty_section(self):
        """Create radio buttons for difficulty levels."""
        difficulty_label = Label(self.window, text="Select the difficulty level:", font=("Arial", 14))
        difficulty_label.pack(pady=10)

        # Radio buttons for difficulty levels
        Radiobutton(self.window, text="Easy", variable=self.difficulty, value="easy").pack(anchor="w", padx=20, pady=5)
        Radiobutton(self.window, text="Normal", variable=self.difficulty, value="normal").pack(anchor="w", padx=20, pady=5)
        Radiobutton(self.window, text="Hard", variable=self.difficulty, value="hard").pack(anchor="w", padx=20, pady=5)

    def create_submit_buttons(self):
        """Create submit buttons for materials and difficulty."""
        submit_button = Button(self.window, text="Submit", command=self.submit_and_close)
        submit_button.pack(pady=20)

    def submit_and_close(self):
        """Handle submission and close the window."""
        self.submit_materials()  # Update material_list
        self.submit_difficulty()  # Update difficulty
        self.is_submitted = True
        self.window.destroy()  # Close the GUI

    def submit_materials(self):
        """Update the selected materials in the material list."""
        self.material_list.clear()
        if self.x.get() == 1:
            self.material_list.append("Kickboard")
        if self.y.get() == 1:
            self.material_list.append("Pull Buoy")
        if self.z.get() == 1:
            self.material_list.append("Fins")
        if self.w.get() == 1:
            self.material_list.append("Paddles")
        return self.material_list

    def submit_difficulty(self):
        """Return the selected difficulty."""
        return self.difficulty.get()

    def get_values(self):
        """Return selected materials and difficulty."""
        return self.material_list, self.difficulty.get()

    def run(self):
        """Run the main event loop."""
        self.window.mainloop()
