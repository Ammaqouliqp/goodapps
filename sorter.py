import os

def main():
    # inster your path
    folder_path = input("inter your path: ")

    # inter file foramt
    file_format = input("inter your file formats for exp : .txt or .png... ")

    # list all of the file in folder
    file_list = [file for file in os.listdir(folder_path) if file.endswith(file_format)]

    # count of files
    num_files = len(file_list)
    print(f"number of files: {num_files}")

    # rename the all files
    for i, file_name in enumerate(file_list, start=1):
        new_file_name = f"{i}{file_format}"
        os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))
        print(f"file {file_name} to {new_file_name} renamed.")

if __name__ == "__main__":
    main()
