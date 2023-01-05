import os, cv2
from fastdlo.core import Pipeline


if __name__ == "__main__":

    ######################
    dir = "/home/hollydinkel/COCOpen/datasets/cocopen-dataset/val"
    ckpt_siam_name = "CP_similarity.pth"
    ckpt_seg_name = "CP_segmentation.pth"
    IMG_W = 1920
    IMG_H = 1080
    ######################

    for file in os.listdir(dir):
        script_path = os.path.dirname(os.path.realpath(__file__))
        checkpoint_siam = os.path.join(script_path, "weights/" + ckpt_siam_name)
        checkpoint_seg = os.path.join(script_path, "weights/" + ckpt_seg_name)
        

        p = Pipeline(checkpoint_siam=checkpoint_siam, checkpoint_seg=checkpoint_seg, img_w=IMG_W, img_h=IMG_H)

        # COLOR
        source_img = cv2.imread(IMG_PATH, cv2.IMREAD_COLOR)
        source_img = cv2.resize(source_img, (IMG_W, IMG_H))

        img_out, _ = p.run(source_img=source_img, mask_th=77)

        canvas = source_img.copy()
        canvas = cv2.addWeighted(canvas, 1.0, img_out, 0.8, 0.0)
        
        cv2.imwrite(f"./predictions/{file}",canvas)
