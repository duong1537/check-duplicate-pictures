import os
import cv2
import time

from multiprocessing import Pool, cpu_count

path = "./images_in"
image_files = [os.path.join(path, f) for f in os.listdir(path) if
               os.path.isfile(os.path.join(path, f)) and f.endswith(('.png', '.jpg', '.jpeg', '.bmp'))]

def compare_images(pair):
    i, j = pair
    # Đọc ảnh từ file
    img1 = cv2.imread(image_files[i])
    img2 = cv2.imread(image_files[j])
    # Tính toán chỉ số SSIM
    ssim_score = cv2.compareHist(cv2.calcHist([img1], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256]),
                                 cv2.calcHist([img2], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256]),
                                 cv2.HISTCMP_CORREL)
    #calcHist(img, tham số màu RGB, vùng cụ thể, size bin color, range index color)
    if ssim_score > 0.95:
        return 1
    return 0

if __name__ == '__main__':
    max_num_images = len(image_files)
    for num_images in range(1, max_num_images + 1):
        start_time = time.time()  # Lấy thời điểm bắt đầu chạy code
        pairs = [(i, j) for i in range(num_images) for j in range(i + 1, num_images)]
        with Pool(processes=cpu_count()) as pool:
            results = pool.map(compare_images, pairs)
        num_duplicates = sum(results)
        end_time = time.time()  # Lấy thời điểm kết thúc chạy code
        elapsed_time = end_time - start_time  # Tính thời gian chạy code
        print("Số bức ảnh: %d - Số ảnh trùng lặp: %d - Thời gian chạy code: %.2f giây" % (num_images, num_duplicates, elapsed_time))


