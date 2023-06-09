# Yolov7 Segmentation 

### Dataset 
```
Data name: PRJ003_Area1
Data label: ['car', 'house', 'lake', 'tree']
```

## Steps to run Code

- Clone the repository
```
git clone https://github.com/vunguyen1998/trainYoloV7.git
```
- Go to the cloned folder.
```
cd trainYoloV7
```
- Create a virtual envirnoment (Recommended, If you dont want to disturb python packages)
```
### For Linux Users
python3 -m venv yolov7seg
source yolov7seg/bin/activate

### For Window Users
python3 -m venv yolov7seg
cd yolov7seg
cd Scripts
activate
cd ..
cd ..
```
- Upgrade pip with mentioned command below.
```
pip install --upgrade pip
```
- Install requirements with mentioned command below.
```
pip install -r requirements.txt
```

- Run the code with mentioned command below.
```
#for segmentation with detection
python3 segment/predict.py --weights "runs/train-seg/yolov7-seg2/weights/best.pt" --source "test.jpg"

#for segmentation with detection + Tracking
python3 segment/predict.py --weights "runs/train-seg/yolov7-seg2/weights/best.pt" --source "test.jpg" --trk

#save the labels files of segmentation
python3 segment/predict.py --weights "runs/train-seg/yolov7-seg2/weights/best.pt" --source "test.jpg" --save-txt
```

- Output file will be created in the working directory with name `./runs/predict-seg/exp/test.jpg`


## Custom Training

- Move your (segmentation custom labelled data) inside "yolov7-segmentation\data" folder by following mentioned structure.

![ss](https://user-images.githubusercontent.com/62513924/190388927-62a3ee84-bad8-4f59-806f-1185acdc8acb.png)



- Go to the <b>data</b> folder, create a file with name <b>data.yaml</b> and paste the mentioned code below inside that.

```
train: data/train/images
val: data/valid/images

nc: 4
names: ['car', 'house', 'lake', 'tree']
```
## Train Model Segmentation
```
python3 segment/train.py --data data/data.yaml --batch 2 --weights yolov7-seg.pt --cfg models/segment/yolov7-seg.yaml --epochs 100 --name yolov7-seg --hyp hyps/hyp.scratch-high.yaml

```

## Run Model Segmentation
```
python3 segment/predict.py --weights "runs/train-seg/yolov7-seg2/weights/best.pt" --name output --source "test.jpg"
```

## RESULTS
<style>
.result {
  width: 100%;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
}
.result img {
  width: 80%;
  min-width: 480px;
  max-width: 640px;

}
</style>
<div class="result">
  <img src="/runs/train-seg/yolov7-seg/val_batch0_pred.jpg">
  <img src="/runs/train-seg/yolov7-seg/val_batch1_pred.jpg">
  <img src="/runs/train-seg/yolov7-seg/val_batch2_pred.jpg">
</div>


## References
- https://github.com/WongKinYiu/yolov7/tree/u7/seg
