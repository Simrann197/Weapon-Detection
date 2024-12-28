import os

# Define the paths
temp_folder_path = 'E:/Weapon-Detection/temp'  # Path to the temp folder
train_folder_path = os.path.join(temp_folder_path, 'train')  # Path for training images
val_folder_path = os.path.join(temp_folder_path, 'val')  # Path for validation images

# Define the labels (0 for Gun, 1 for Knife)
labels = {'gun': 0, 'knife': 1}

# Create labels folder structure
labels_train_folder = os.path.join(temp_folder_path, 'labels', 'train')
labels_val_folder = os.path.join(temp_folder_path, 'labels', 'val')

os.makedirs(labels_train_folder, exist_ok=True)
os.makedirs(labels_val_folder, exist_ok=True)

# Function to create label files in YOLO format
def create_txt_file(image_path, label_class):
    # Create corresponding .txt file
    txt_file_path = image_path.replace('.jpg', '.txt')
    with open(txt_file_path, 'w') as f:
        # Example dummy values for bounding box (center x, center y, width, height) in normalized form
        # Replace this with actual bounding box coordinates if available
        f.write(f"{label_class} 0.5 0.5 0.4 0.4\n")  # Dummy values

# Process all train images
for image in os.listdir(train_folder_path):
    if image.endswith('.jpg'):
        # Determine the label based on the image filename
        label_class = 0 if 'gun' in image.lower() else 1  # Assuming 'gun' or 'knife' in filename
        
        # Create the .txt file for the image in the correct directory
        image_path = os.path.join(train_folder_path, image)
        create_txt_file(os.path.join(labels_train_folder, image), label_class)

# Process all validation images
for image in os.listdir(val_folder_path):
    if image.endswith('.jpg'):
        # Determine the label based on the image filename
        label_class = 0 if 'gun' in image.lower() else 1  # Assuming 'gun' or 'knife' in filename
        
        # Create the .txt file for the image in the correct directory
        image_path = os.path.join(val_folder_path, image)
        create_txt_file(os.path.join(labels_val_folder, image), label_class)

print("Label files (.txt) have been created successfully.")












# import os

# # Specify the path to your guns images folder
# folder_path = 'E:\Weapon-Detection\Knife'  # Replace this with the actual path

# # Get all files in the folder
# files = os.listdir(folder_path)

# # Filter out non-image files (optional, in case your folder has other files)
# image_files = [file for file in files if file.lower().endswith(('.jpg', '.jpeg', '.png'))]

# # Sort files if needed (optional)
# image_files.sort()

# # Rename the files
# for idx, file_name in enumerate(image_files, start=1):
#     # Get the file extension (e.g., .jpg, .png)
#     file_extension = os.path.splitext(file_name)[1]
    
#     # Create the new file name
#     new_name = f'knife{idx}{file_extension}'
    
#     # Construct the full file paths
#     old_file_path = os.path.join(folder_path, file_name)
#     new_file_path = os.path.join(folder_path, new_name)
    
#     # Rename the file
#     os.rename(old_file_path, new_file_path)
#     print(f'Renamed: {file_name} -> {new_name}')





# import os
# import random
# import shutil

# # Define paths for the temp folder and the new train/val folders
# temp_folder_path = 'E:\\Weapon-Detection\\temp'  # Replace this with the actual path to your "temp" folder
# train_folder_path = 'E:\\Weapon-Detection\\temp\\train'  # Replace with the path where you want to store train images
# val_folder_path = 'E:\\Weapon-Detection\\temp\\val'  # Replace with the path where you want to store val images

# # Create the train and val folders if they don't exist
# os.makedirs(train_folder_path, exist_ok=True)
# os.makedirs(val_folder_path, exist_ok=True)

# # Get all files in the "temp" folder
# all_files = [file for file in os.listdir(temp_folder_path) if file.lower().endswith(('.jpg', '.jpeg', '.png'))]

# # Shuffle the files for random splitting
# random.shuffle(all_files)

# # Define the proportion for train and val (e.g., 80% train, 20% val)
# train_size = int(0.8 * len(all_files))  # 80% for training
# val_size = len(all_files) - train_size  # Remaining 20% for validation

# # Split the files into train and val
# train_files = all_files[:train_size]
# val_files = all_files[train_size:]

# # Move the files to the appropriate directories
# for file in train_files:
#     shutil.move(os.path.join(temp_folder_path, file), os.path.join(train_folder_path, file))

# for file in val_files:
#     shutil.move(os.path.join(temp_folder_path, file), os.path.join(val_folder_path, file))

# print(f"Moved {len(train_files)} files to the train folder.")
# print(f"Moved {len(val_files)} files to the val folder.")
