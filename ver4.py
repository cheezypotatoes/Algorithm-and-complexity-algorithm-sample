import tkinter as tk
from tkinter import ttk
import time

def insertion_sort(arr, log_text):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        
        log_text.insert(tk.END, f"  Inserted {key} at position {j+1}: {arr}\n", "log")  # FOR LOGGING
    log_text.insert(tk.END, f"\nFinal Sorted Array: {arr}\n", "final")
    log_text.insert(tk.END, "Time Complexity: O(n^2) in worst/average case, O(n) best case\n", "final")

def bubble_sort(arr, log_text):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
        log_text.insert(tk.END, f"After pass {i+1}: {arr}\n", "log")  # FOR LOGGING
    log_text.insert(tk.END, f"\nFinal Sorted Array: {arr}\n", "final")
    log_text.insert(tk.END, "Time Complexity: O(n^2) in worst/average case, O(n) best case\n", "final")

def selection_sort(arr, log_text):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        # log_text.insert(tk.END, f"Pass {i+1}: {arr}\n", "log")  # FOR LOGGING
        print(f"Pass {i+1}: {arr}")  # PRINT STATEMENT
    log_text.insert(tk.END, f"\nFinal Sorted Array: {arr}\n", "final")
    log_text.insert(tk.END, "Time Complexity: O(n^2) in all cases\n", "final")

def perform_sort():
    input_data = entry.get()
    try:
        arr = list(map(int, input_data.split(',')))
    except ValueError:
        log_text.config(state=tk.NORMAL)
        log_text.delete("1.0", tk.END)
        log_text.insert(tk.END, "Invalid input! Please enter a comma-separated list of numbers.\n", "error")
        log_text.config(state=tk.DISABLED)
        return
    
    log_text.config(state=tk.NORMAL)
    log_text.delete("1.0", tk.END)
    log_text.insert(tk.END, f"Original Array: {arr}\n", "title")
    
    start_time = time.time()
    
    if sort_method.get() == "Insertion Sort":
        insertion_sort(arr, log_text)
    elif sort_method.get() == "Bubble Sort":
        bubble_sort(arr, log_text)
    elif sort_method.get() == "Selection Sort":
        selection_sort(arr, log_text)
    
    elapsed_time = time.time() - start_time
    log_text.insert(tk.END, f"\nExecution Time: {elapsed_time:.7f} seconds\n", "final")
    log_text.config(state=tk.DISABLED)

# GUI Setup
root = tk.Tk()
root.title("Sorting Algorithm Visualization")
root.geometry("600x550")
root.configure(bg="#282C34")

style = ttk.Style()
style.configure("TButton", font=("Arial", 10), padding=3)
style.configure("TLabel", font=("Arial", 10), background="#282C34", foreground="white")

frame = tk.Frame(root, bg="#3C3F41", padx=10, pady=10)
frame.pack(expand=True, fill=tk.BOTH)

tk.Label(frame, text="Sorting Algorithm Visualization", font=("Arial", 12, "bold"), bg="#3C4048", fg="white").pack()

tk.Label(frame, text="Enter numbers (comma-separated):", bg="#3C3F41", fg="white").pack()
entry = tk.Entry(frame, width=40, font=("Arial", 10))
entry.pack(pady=6)

sort_method = tk.StringVar(value="Insertion Sort")
ttk.Radiobutton(frame, text="Insertion Sort", variable=sort_method, value="Insertion Sort").pack(pady=2)
ttk.Radiobutton(frame, text="Bubble Sort", variable=sort_method, value="Bubble Sort").pack(pady=2)
ttk.Radiobutton(frame, text="Selection Sort", variable=sort_method, value="Selection Sort").pack(pady=2)

log_text = tk.Text(frame, height=20, width=70, bg="#1E2128", fg="lightgreen", font=("Consolas", 8))
log_text.pack(pady=6)
log_text.tag_config("title", font=("Arial", 9, "bold"), foreground="cyan")
log_text.tag_config("log", foreground="lightgray")
log_text.tag_config("final", foreground="lightgreen")
log_text.tag_config("error", foreground="red")

btn_sort = ttk.Button(frame, text="Sort Array", command=perform_sort)
btn_sort.pack(pady=6)

root.mainloop()