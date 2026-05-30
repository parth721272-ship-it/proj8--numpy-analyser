import numpy as np

class DataAnalytics:
    def __init__(self):
        self.array = None

    def create_array(self):
        while True:
            print("\nArray Creation:")
            print("1. 1D Array")
            print("2. 2D Array")
            print("3. 3D Array")
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                size = int(input("Enter the size of the array: "))
                elements = list(map(int, input(f"Enter {size} elements for the array separated by space: ").split()))
                self.array = np.array(elements)
                break
            elif choice == 2:
                rows = int(input("Enter the number of rows: "))
                cols = int(input("Enter the number of columns: "))
                elements = list(map(int, input(f"Enter {rows*cols} elements for the array separated by space: ").split()))
                self.array = np.array(elements).reshape(rows, cols)
                break
            elif choice == 3:
                depth = int(input("Enter the depth: "))
                rows = int(input("Enter the number of rows: "))
                cols = int(input("Enter the number of columns: "))
                elements = list(map(int, input(f"Enter {depth*rows*cols} elements for the array separated by space: ").split()))
                self.array = np.array(elements).reshape(depth, rows, cols)
                break
            else:
                print("Invalid choice! Please try again.")

    def array_management(self):
        if self.array is None:
            print("Please create an array first!")
            return
        
        while True:
            print("\nChoose an operation:")
            print("1. Indexing")
            print("2. Slicing")
            print("3. Go Back")
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                index = int(input("Enter the index: "))
                print(self.array[index])
            elif choice == 2:
                row_start, row_end = map(int, input("Enter the row range (start:end): ").split())
                col_start, col_end = map(int, input("Enter the column range (start:end): ").split())
                print(self.array[row_start:row_end, col_start:col_end])
            elif choice == 3:
                break
            else:
                print("Invalid choice! Please try again.")

    def mathematical_operations(self):
        if self.array is None:
            print("Please create an array first!")
            return
        
        while True:
            print("\nMathematical Operations:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Go Back")
            choice = int(input("Enter your choice: "))
            
            if choice in [1, 2, 3, 4]:
                elements = list(map(int, input("Enter the same-size array elements (6 elements separated by space): ").split()))
                other_array = np.array(elements).reshape(self.array.shape)
                if choice == 1:
                    print(f"Result of Addition:\n{self.array + other_array}")
                elif choice == 2:
                    print(f"Result of Subtraction:\n{self.array - other_array}")
                elif choice == 3:
                    print(f"Result of Multiplication:\n{self.array * other_array}")
                elif choice == 4:
                    print(f"Result of Division:\n{self.array / other_array}")
            elif choice == 5:
                break
            else:
                print("Invalid choice! Please try again.")

    def combine_split_arrays(self):
        if self.array is None:
            print("Please create an array first!")
            return
        
        while True:
            print("\nCombine or Split Arrays:")
            print("1. Combine Arrays")
            print("2. Split Array")
            print("3. Go Back")
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                elements = list(map(int, input("Enter the elements of another array to combine (6 elements separated by space): ").split()))
                other_array = np.array(elements).reshape(self.array.shape)
                print(f"Combined Array (Vertical Stack):\n{np.vstack((self.array, other_array))}")
            elif choice == 2:
                parts = int(input("Enter the number of parts to split: "))
                split_arrays = np.array_split(self.array, parts)
                for i, arr in enumerate(split_arrays):
                    print(f"Split Array {i+1}:\n{arr}")
            elif choice == 3:
                break
            else:
                print("Invalid choice! Please try again.")

    def search_sort_filter(self):
        if self.array is None:
            print("Please create an array first!")
            return
        
        while True:
            print("\nSearch, Sort, and Filter:")
            print("1. Search a value")
            print("2. Sort the array")
            print("3. Filter values")
            print("4. Go Back")
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                value = int(input("Enter the value to search: "))
                indices = np.where(self.array == value)
                print(f"Indices where {value} is found: {indices}")
            elif choice == 2:
                sorted_array = np.sort(self.array)
                print(f"Sorted Array:\n{sorted_array}")
            elif choice == 3:
                condition = input("Enter condition (e.g., >10): ")
                filtered_array = self.array[eval(f"self.array {condition}")]
                print(f"Filtered Array:\n{filtered_array}")
            elif choice == 4:
                break
            else:
                print("Invalid choice! Please try again.")

    def aggregates_statistics(self):
        if self.array is None:
            print("Please create an array first!")
            return
        
        while True:
            print("\nAggregates and Statistics:")
            print("1. Sum")
            print("2. Mean")
            print("3. Median")
            print("4. Standard Deviation")
            print("5. Variance")
            print("6. Go Back")
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                print(f"Sum of Array: {np.sum(self.array)}")
            elif choice == 2:
                print(f"Mean of Array: {np.mean(self.array)}")
            elif choice == 3:
                print(f"Median of Array: {np.median(self.array)}")
            elif choice == 4:
                print(f"Standard Deviation of Array: {np.std(self.array)}")
            elif choice == 5:
                print(f"Variance of Array: {np.var(self.array)}")
            elif choice == 6:
                break
            else:
                print("Invalid choice! Please try again.")

def main():
    analyzer = DataAnalytics()
    while True:
        print("\nWelcome to the NumPy Analyzer!")
        print("=================================")
        print("Choose an option:")
        print("1. Create a NumPy Array")
        print("2. Perform Mathematical Operations")
        print("3. Combine or Split Arrays")
        print("4. Search, Sort, or Filter Arrays")
        print("5. Compute Aggregates and Statistics")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            analyzer.create_array()
        elif choice == 2:
            analyzer.mathematical_operations()
        elif choice == 3:
            analyzer.combine_split_arrays()
        elif choice == 4:
            analyzer.search_sort_filter()
        elif choice == 5:
            analyzer.aggregates_statistics()
        elif choice == 6:
            print("Thank you for using the NumPy Analyzer! Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()