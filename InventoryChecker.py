import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

class AssetInventorySystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Asset Inventory System - Viewer")
        self.root.geometry("900x600")
        self.root.resizable(False, False)
        
        # Credentials (in a real system, these would be stored securely)
        self.valid_credentials = {
            "admin": "N3w1nv3n70ryP455w0rd123"
        }
        
        # Hardcoded asset database
        self.assets = [
            {
                "AssetID": "Sample",
                "hostname": "Sample",
                "ip": "Sample",
                "server_version": "Sample",
                "location": "Sample",
                "os": "Sample",
                "cpu": "Sample",
                "ram": "Sample",
                "storage": "Sample",
                "status": "Sample",
                "last_backup": "Sample",
                "notes": "Sample"
            }
        ]
        
        # Create login frame
        self.login_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.login_frame.pack(fill=tk.BOTH, expand=True)
        
        self.create_login_widgets()
        
    def create_login_widgets(self):
        # Login header
        header = tk.Label(
            self.login_frame, 
            text="Asset Inventory System", 
            font=("Arial", 20, "bold"),
            bg="#f0f0f0",
            fg="#2c3e50"
        )
        header.pack(pady=30)
        
        # Login frame container
        login_container = tk.Frame(self.login_frame, bg="#f0f0f0")
        login_container.pack(pady=20)
        
        # Username
        tk.Label(
            login_container, 
            text="Username:", 
            font=("Arial", 12),
            bg="#f0f0f0"
        ).grid(row=0, column=0, padx=10, pady=10, sticky="e")
        
        self.username_entry = tk.Entry(
            login_container, 
            font=("Arial", 12),
            width=20
        )
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)
        self.username_entry.bind('<Return>', lambda e: self.login())
        
        # Password
        tk.Label(
            login_container, 
            text="Password:", 
            font=("Arial", 12),
            bg="#f0f0f0"
        ).grid(row=1, column=0, padx=10, pady=10, sticky="e")
        
        self.password_entry = tk.Entry(
            login_container, 
            font=("Arial", 12),
            width=20,
            show="*"
        )
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)
        self.password_entry.bind('<Return>', lambda e: self.login())
        
        # Login button
        login_btn = tk.Button(
            self.login_frame,
            text="Login",
            font=("Arial", 12, "bold"),
            bg="#3498db",
            fg="white",
            width=15,
            height=1,
            command=self.login
        )
        login_btn.pack(pady=20)
        
        # Status label
        self.status_label = tk.Label(
            self.login_frame,
            text="",
            font=("Arial", 10),
            bg="#f0f0f0",
            fg="red"
        )
        self.status_label.pack(pady=5)
        
        # Footer
        footer = tk.Label(
            self.login_frame,
            text="© 2026 Asset Inventory System",
            font=("Arial", 9),
            bg="#f0f0f0",
            fg="#7f8c8d"
        )
        footer.pack(side=tk.BOTTOM, pady=20)
        
    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        
        if not username or not password:
            self.status_label.config(text="Please enter both username and password", fg="red")
            return
        
        if username in self.valid_credentials and self.valid_credentials[username] == password:
            self.status_label.config(text="Login successful!", fg="green")
            self.root.after(500, self.show_main_screen)
        else:
            self.status_label.config(text="Invalid credentials. Please try again.", fg="red")
            self.password_entry.delete(0, tk.END)
            self.password_entry.focus()
    
    def show_main_screen(self):
        # Destroy login frame
        self.login_frame.destroy()
        
        # Create main frame
        self.main_frame = tk.Frame(self.root, bg="#ecf0f1")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Welcome header
        welcome_frame = tk.Frame(self.main_frame, bg="#2c3e50", height=60)
        welcome_frame.pack(fill=tk.X)
        welcome_frame.pack_propagate(False)
        
        welcome_label = tk.Label(
            welcome_frame,
            text="Asset Inventory Viewer",
            font=("Arial", 16, "bold"),
            bg="#2c3e50",
            fg="white"
        )
        welcome_label.pack(side=tk.LEFT, padx=20, pady=18)
        
        # Logout button in header
        logout_btn = tk.Button(
            welcome_frame,
            text="Logout",
            font=("Arial", 10, "bold"),
            bg="#e74c3c",
            fg="white",
            width=10,
            height=1,
            command=self.logout
        )
        logout_btn.pack(side=tk.RIGHT, padx=20, pady=15)
        
        # Total assets count
        count_label = tk.Label(
            welcome_frame,
            text=f"Total Assets: {len(self.assets)}",
            font=("Arial", 12),
            bg="#2c3e50",
            fg="#ecf0f1"
        )
        count_label.pack(side=tk.RIGHT, padx=20)
        
        
        # Create treeview frame
        tree_frame = tk.Frame(self.main_frame, bg="#ecf0f1")
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create scrollbar
        scrollbar = ttk.Scrollbar(tree_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Create treeview with all columns
        columns = (
            "AssetID", "Hostname", "IP Address", "Server Version", "Location", 
            "OS", "CPU", "RAM", "Storage", "Status", "Last Backup", "Notes"
        )
        
        self.tree = ttk.Treeview(
            tree_frame,
            columns=columns,
            show="headings",
            yscrollcommand=scrollbar.set,
            height=20
        )
        
        # Configure scrollbar
        scrollbar.config(command=self.tree.yview)
        
        
        # Set column headings and widths
        column_widths = {
            "AssetID": 78,
            "Hostname": 80,
            "IP Address": 105,
            "Server Version": 100,
            "Location": 100,
            "OS": 120,
            "CPU": 120,
            "RAM": 80,
            "Storage": 80,
            "Status": 80,
            "Last Backup": 130,
            "Notes": 200
        }
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=column_widths.get(col, 100), minwidth=10, anchor="w", stretch=False)
        
        # Insert all assets into treeview
        for asset in self.assets:
            self.tree.insert(
                "",
                "end",
                values=(
                    asset["AssetID"],
                    asset["hostname"],
                    asset["ip"],
                    asset["server_version"],
                    asset["location"],
                    asset["os"],
                    asset["cpu"],
                    asset["ram"],
                    asset["storage"],
                    asset["status"],
                    asset["last_backup"],
                    asset["notes"]
                )
            )
        
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        # Status bar
        status_frame = tk.Frame(self.main_frame, bg="#34495e", height=30)
        status_frame.pack(fill=tk.X, side=tk.BOTTOM)
        status_frame.pack_propagate(False)
        
        status_label = tk.Label(
            status_frame,
            text=f"Showing {len(self.assets)} assets | Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            font=("Arial", 9),
            bg="#34495e",
            fg="white"
        )
        status_label.pack(side=tk.LEFT, padx=20, pady=5)
        
        # Search/Filter functionality
        search_frame = tk.Frame(self.main_frame, bg="#ecf0f1")
        search_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(
            search_frame,
            text="Search:",
            font=("Arial", 10),
            bg="#ecf0f1"
        ).pack(side=tk.LEFT, padx=5)
        
        self.search_entry = tk.Entry(
            search_frame,
            font=("Arial", 10),
            width=30
        )
        self.search_entry.pack(side=tk.LEFT, padx=5)
        self.search_entry.bind('<KeyRelease>', self.search_assets)
        
        tk.Button(
            search_frame,
            text="Clear Search",
            font=("Arial", 9),
            bg="#95a5a6",
            fg="white",
            command=self.clear_search
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Label(
            search_frame,
            text="Click column header to sort",
            font=("Arial", 9, "italic"),
            bg="#ecf0f1",
            fg="#7f8c8d"
        ).pack(side=tk.RIGHT, padx=10)
    
    def search_assets(self, event=None):
        """Search and filter assets based on search entry"""
        search_term = self.search_entry.get().strip().lower()
        
        # Clear current treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        if not search_term:
            # Show all assets
            for asset in self.assets:
                self.tree.insert(
                    "",
                    "end",
                    values=(
                    	asset["AssetID"],
                        asset["hostname"],
                        asset["ip"],
                        asset["server_version"],
                        asset["location"],
                        asset["os"],
                        asset["cpu"],
                        asset["ram"],
                        asset["storage"],
                        asset["status"],
                        asset["last_backup"],
                        asset["notes"]
                    )
                )
        else:
            # Show only matching assets
            for asset in self.assets:
                # Search in all fields
                if any(search_term in str(value).lower() for value in asset.values()):
                    self.tree.insert(
                        "",
                        "end",
                        values=(
                            asset["AssetID"],
                            asset["hostname"],
                            asset["ip"],
                            asset["server_version"],
                            asset["location"],
                            asset["os"],
                            asset["cpu"],
                            asset["ram"],
                            asset["storage"],
                            asset["status"],
                            asset["last_backup"],
                            asset["notes"]
                        )
                    )
    
    def clear_search(self):
        """Clear search box and show all assets"""
        self.search_entry.delete(0, tk.END)
        self.search_assets()
    
    def logout(self):
        # Confirm logout
        if messagebox.askyesno("Logout", "Are you sure you want to logout?"):
            self.main_frame.destroy()
            self.login_frame = tk.Frame(self.root, bg="#f0f0f0")
            self.login_frame.pack(fill=tk.BOTH, expand=True)
            self.create_login_widgets()

def main():
    root = tk.Tk()
    app = AssetInventorySystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()
