##🖼️ Image Duplicate Detection and Performance Evaluation

This project provides Python scripts to detect duplicate images and to compare the performance of different approaches (single-core, multithreading, and multiprocessing).

##📂 Project Structure

CompareHistory_multithread.py – Compares images for duplicates using multithreading.

CompareHistory_SingleCore.py – Compares images for duplicates on a single core without parallelism.

data_gen_multiprocessing.py – Generates performance data for duplicate detection using multiprocessing.

data_gen_multithreading.py – Generates performance data for duplicate detection using multithreading and plots execution time.

data_gen_single_core.py – Generates performance data for duplicate detection on a single core.

detect_multiprocessing.py – Detects duplicate images in a folder using multiprocessing.

detect_multithreading.py – Detects duplicate images in a folder using multithreading.

Single_Core.py – Detects duplicate images in a folder on a single core.

##▶️ Usage

#1. Place your images inside the corresponding input folder (e.g., ./images_in or ./data).

#2. Run the desired script:

python detect_multithreading.py


or

python detect_multiprocessing.py


#3. For performance evaluation, run one of the data_gen_* scripts to see execution time growth with the number of images.