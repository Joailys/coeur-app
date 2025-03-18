import tkinter as tk
import random
import time
import platform

class HeartAnimation:
    def __init__(self):
        self.root = tk.Tk()
        
        # Configuration multi-OS
        if platform.system() == 'Darwin':
            self.root.attributes('-fullscreen', True)
            self.root.configure(menu=tk.Menu(self.root))  # Désactive la barre de menu
        else:
            self.root.attributes('-fullscreen', True, '-topmost', True)
        
        self.canvas = tk.Canvas(self.root, bg='black', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.start_time = time.time()
        self.animate()
        self.root.mainloop()
    
    def create_heart(self):
        x = random.randint(0, self.root.winfo_screenwidth())
        y = random.randint(0, self.root.winfo_screenheight())
        colors = ['#FF69B4', '#FF1493', '#FF6B6B']
        
        self.canvas.create_text(
            x, y,
            text='♥',
            font=('Arial', random.randint(30, 80)),
            fill=random.choice(colors),
            anchor='center'
        )
    
    def animate(self):
        if time.time() - self.start_time < 5:
            self.create_heart()
            self.root.after(50, self.animate)
        else:
            self.root.destroy()

if __name__ == "__main__":
    HeartAnimation()
