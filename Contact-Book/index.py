import tkinter as tk
from tkinter import ttk, messagebox

class ContactApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contacts = []

        self.create_widgets()
        self.apply_styles()

    def create_widgets(self):
        # Input Fields
        self.name_label = tk.Label(self.root, text="Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.phone_label = tk.Label(self.root, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        self.email_label = tk.Label(self.root, text="Email:")
        self.email_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.email_entry = tk.Entry(self.root)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        self.address_label = tk.Label(self.root, text="Address:")
        self.address_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.address_entry = tk.Entry(self.root)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5)

        # Buttons
        self.add_button = ttk.Button(self.root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="we")
        self.update_button = ttk.Button(self.root, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="we")
        self.delete_button = ttk.Button(self.root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="we")

        # Contact List
        self.contact_listbox = tk.Listbox(self.root, width=80, height=10)
        self.contact_listbox.grid(row=7, column=0, columnspan=2, padx=5, pady=20)

    def apply_styles(self):
        style = ttk.Style()

        # Entry Style
        style.configure('TEntry', font=('Arial', 12), padding=5, relief=tk.SOLID, borderwidth=2)

        # Button Style
        style.configure('Add.TButton', font=('Arial', 12), foreground='white', background='#007bff', padding=10)
        style.map('Add.TButton', background=[('active', '#0056b3')])
        style.configure('Update.TButton', font=('Arial', 12), foreground='white', background='#ffc107', padding=10)
        style.map('Update.TButton', background=[('active', '#e0a800')])
        style.configure('Delete.TButton', font=('Arial', 12), foreground='white', background='#dc3545', padding=10)
        style.map('Delete.TButton', background=[('active', '#c82333')])

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            self.contacts.append({"Name": name, "Phone": phone, "Email": email, "Address": address})
            messagebox.showinfo("Success", "Contact added successfully")
            self.update_contact_listbox()
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Name and Phone are required fields")

    def update_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            selected_contact_index = selected_index[0]
            selected_contact = self.contacts[selected_contact_index]

            # Update the selected contact with the new details from the input fields
            selected_contact["Name"] = self.name_entry.get()
            selected_contact["Phone"] = self.phone_entry.get()
            selected_contact["Email"] = self.email_entry.get()
            selected_contact["Address"] = self.address_entry.get()

            messagebox.showinfo("Success", "Contact updated successfully")
            self.update_contact_listbox()  # Update the contact listbox
        else:
            messagebox.showerror("Error", "Please select a contact from the list")

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            self.contacts.pop(selected_index[0])
            messagebox.showinfo("Success", "Contact deleted successfully")
            self.update_contact_listbox()
        else:
            messagebox.showerror("Error", "Please select a contact from the list")

    def update_contact_listbox(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            contact_info = f"Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}, Address: {contact['Address']}"
            self.contact_listbox.insert(tk.END, contact_info)

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactApp(root)
    root.mainloop()
