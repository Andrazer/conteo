

## 💻 install

- setup python environment and activate it [optional]

    ```bash
    venv\Scripts\activate
    deactivate
    ```

- install required dependencies

    ```bash
    pip install -r requirements.txt
    ```



## ⚙️ run

```bash
python conteo.py --webcam-resolution 640, 360 --source_weights_path yolov8l.pt 
#--source_video_path video.mp4 --confidence_threshold 0.3 --iou_threshold 0.5 --target_video_path result.mov
```