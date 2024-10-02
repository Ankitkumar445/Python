import os


def print_directory_contents(path):
    try:
        # List all files and directories in the specified path
        items = os.listdir(path)

        print(f"Contents of '{path}':")
        for item in items:
            # Get the full path
            full_path = os.path.join(path, item)
            # Check if it's a file or a directory
            if os.path.isdir(full_path):
                print(f"[DIR]  {item}")
            else:
                print(f"[FILE] {item}")
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Change this to the directory you want to list
directory_path = input("Enter the directory path: ")
print_directory_contents(directory_path)
