import argparse
import supervision as sv
from ultralytics import YOLO

import cv2

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description = "Yolov8 live")
    parser.add_argument(
        "--webcam-resolution",
        default =[1280, 720],
        nargs = 2,
        type =int,
    )
    parser.add_argument(
        "--source_weights_path",
        default = "yolov8n.pt",
        help="Path to the source weights file",
        type=str,
    )

    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    frame_width, frame_height = args.webcam_resolution
    source_weights_path = args.source_weights_path

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

    model = YOLO(source_weights_path)

    box_annotator = sv.BoxAnnotator(
        thickness = 2,
        text_thickness = 2,
        text_scale = 1
    )

    while True:
        ret, frame = cap.read()

        result = model(frame)[0]
        detections = sv.Detections.from_yolov8(result)
        
        #labels = [f"{model.model.names[class_id]} {confidence:0.2f}" for _ , confidence, class_id, _ in detections]

        frame = box_annotator.annotate(
            scene = frame,
            detections = detections,
            #labels = labels
        )

        cv2.imshow("Analizando imagen con YOLOv8", frame)

        if (cv2.waitKey(30) == 27):
            break

if __name__ == '__main__':
    main()
