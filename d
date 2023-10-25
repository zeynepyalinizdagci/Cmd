import os
import shutil
import datetime

def delete_old_directories(base_path, num_to_keep):
    # Get a list of all directories in the base path
    directories = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]

    # Sort directories by modification time (oldest first)
    directories.sort(key=lambda x: os.path.getmtime(os.path.join(base_path, x)))

    # Keep the newest 'num_to_keep' directories
    directories_to_keep = directories[-num_to_keep:]

    for directory in directories:
        directory_path = os.path.join(base_path, directory)

        if directory not in directories_to_keep:
            if os.path.isfile(os.path.join(directory_path, 'releases.txt')):
                # If directory has releases.txt, keep it
                continue
            elif os.path.isfile(os.path.join(directory_path, 'alphas.txt')):
                # If directory has alphas.txt, delete it
                shutil.rmtree(directory_path)
                print(f'Deleted: {directory_path}')
            else:
                # If no special files, delete it
                shutil.rmtree(directory_path)
                print(f'Deleted: {directory_path}')

# Example usage:
base_path = '/path/to/your/directory'
num_to_keep = 50

delete_old_directories(base_path, num_to_keep)
