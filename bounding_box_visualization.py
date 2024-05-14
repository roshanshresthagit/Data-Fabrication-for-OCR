import glob
import cv2 as cv
import os

import numpy as np

if __name__ == '__main__':
    '''
    Give the output directiory here for visualization
    '''
    data_dir =r"C:\Users\shres\OneDrive\Desktop\Office\data_fabrication\Text-Fabrication\output"
    ##output directory generated after runing main.py
    # data_dir = "data/Aug2"

    if os.path.exists(data_dir) is False:
        raise Exception("The data directory does not exist.")

    txt_files = glob.glob(os.path.join(data_dir, "*.txt"))

    for file in txt_files:
        image_path = file.replace(".txt", ".jpg")
        image_path = image_path.replace("gt_", "")
        img = cv.imread(image_path)
        with open(file, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                line = line.split(",")
                points = [[int(line[i]), int(line[i+1])] for i in range(0, len(line)-1, 2)]
                points = np.int32(points)
                points = points.reshape((-1, 1, 2))
                cv.polylines(img, [points], True, (0, 0, 255), 2, lineType=cv.LINE_AA)

        cv.imshow("Image", img)
        if cv.waitKey(0) == 27:
            break
        cv.destroyAllWindows()
