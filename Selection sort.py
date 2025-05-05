import matplotlib.pyplot as plt

def selection_sort(arr):
    """
    Perform selection sort and visualize each step including the initial state.
    """
    n = len(arr)

    # Step 0: Show the initial unsorted array
    visualize_selection_sort(arr, step=0, i=-1, min_idx=-1)
    plt.pause(1.0)  # Pause to show the initial array

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        if i != min_idx:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

        visualize_selection_sort(arr, step=i + 1, i=i, min_idx=min_idx)
        plt.pause(0.5)  # Pause between steps

    return arr

def visualize_selection_sort(arr, step, i, min_idx):
    """
    Visualize selection sort progress with color-coded bars.
    Green: Sorted portion
    Red: Minimum element in current pass
    Orange: Element being compared/swapped
    """
    plt.clf()
    colors = []

    for idx in range(len(arr)):
        if i == -1:
            colors.append('lightblue')  # Initial state: all unsorted
        elif idx < i:
            colors.append('lightgreen')  # Sorted portion
        elif idx == min_idx:
            colors.append('red')  # Minimum element
        elif idx == i:
            colors.append('orange')  # Current index
        else:
            colors.append('lightblue')  # Unsorted

    plt.bar(range(len(arr)), arr, color=colors)
    title = "Initial Array (Step 0)" if step == 0 else f"Selection Sort - Step {step}"
    plt.title(title)
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.tight_layout()
    plt.draw()

# Input from user
arr = list(map(int, input("Enter the array to sort (space separated): ").split()))

# Enable interactive plotting
plt.ion()

# Run selection sort with visualization
sorted_arr = selection_sort(arr)

# Final sorted array display
plt.clf()
plt.bar(range(len(arr)), arr, color='lightgreen')
plt.title("Final Sorted Array")
plt.xlabel("Index")
plt.ylabel("Value")
plt.tight_layout()
plt.ioff()
plt.show()

print(f"Sorted Array: {sorted_arr}")
