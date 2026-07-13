import customtkinter as ctk
from Uscanner import scan_url

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("URL Threat Scanner")
        self.geometry("600x350")
        self.resizable(False, False)
        
        self.title_label = ctk.CTkLabel(self, text="URL Scanner", font=("Segoe UI", 22, "bold"))
        self.title_label.pack(pady=(30, 20))
        
        self.url_input = ctk.CTkEntry(self, placeholder_text="Paste link here...", width=500, height=40)
        self.url_input.pack(pady=10)
        
        self.scan_button = ctk.CTkButton(self, text="Analyze Link", width=200, height=40, font=("Segoe UI", 14, "bold"), command=self.run_analysis)
        self.scan_button.pack(pady=15)
        
        self.result_label = ctk.CTkLabel(self, text="Awaiting target URL input...", font=("Segoe UI", 13), text_color="#94a3b8")
        self.result_label.pack(pady=(20, 0))

    def run_analysis(self):
        target = self.url_input.get().strip()
        
        if not target:
            self.result_label.configure(text="Error: Please enter a valid URL path.", text_color="#ef4444")
            return
            
        self.result_label.configure(text="Querying", text_color="#3b82f6")
        self.update_idletasks()
        
        result = scan_url(target)
        
        if result["status"] == "clean":
            self.result_label.configure(text=result["message"], text_color="#10b981")
        elif result["status"] == "dangerous":
            self.result_label.configure(text=result["message"], text_color="#ef4444")
        else:
            self.result_label.configure(text=result["message"], text_color="#ffffff")

if __name__ == "__main__":
    app = App()
    app.mainloop()