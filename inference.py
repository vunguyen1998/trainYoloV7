import gradio as gr
import segment.predict as sp
import csv

from exif import Image

# from segment.sort_count import *
opt = sp.parse_opt()

def input_opt(  source, 
                weights, 
                device,  # cuda device, i.e. 0 or 0,1,2,3 or cpu
            ):
    
    # Get info of image
    def getInfo(img):
        with open(img, 'rb') as image_file:
            my_image = Image(image_file)

        print(my_image.get_all())
    
    # Main options
    opt.weights = f'./runs/train-seg/yolov7-seg/weights/{weights.lower()}.pt'
    if device == True:
        opt.device = '0'
    else:
        opt.device = 'cpu'

    # Advanced options
    opt.save_area = True

    # Create variable 
    names = ['car', 'house', 'lake', 'tree']
    img_target = []
    img_info = []
    area_target = []

    # Loop images input from folder
    for i in source:
        opt.source = i.name
        img, area = sp.main(opt)

        f = open(area, 'r')
        content = f.read()
        line = content.split('\n')
        for j in line:
            if j != '':
                area_in_pic = [i.name.split('/')[4]]
                area_in_pic.append(names[int(j.split(' ')[0])])
                area_in_pic.append(j.split(' ')[1])
            area_target.append(area_in_pic)

        print(i.name)
        img_info.append(getInfo(i.name))
        img_target.append(img)
    
    with open('output.csv', 'w') as f:
        # using csv.writer method from CSV package
        write = csv.writer(f)
        write.writerow(["Picture", "Label", "Area"])
        write.writerows(area_target)

    return img_target, img_info, area_target

def get_select_index(evt: gr.SelectData):
    return evt.index 

with gr.Blocks() as demo:
    with gr.Column():
        folder = gr.File(file_count="directory")
        model_name = gr.Dropdown(
                ["Best", "Last"], value="Best", label="Select model"
            )
        device_select = gr.Checkbox(
                value=True, label="Use GPU"
            )
        btn = gr.Button(value="Submit")

    with gr.Column():
        gallery = gr.Gallery(
            label= 'List target', preview=True
        )
        selected = gr.Text('Select: ')
        gr.HTML('<a href="./output.csv" download="output.csv">Download DataFrame</a>')
        tables = gr.Dataframe(
                headers=["Picture", "Label", "Area"],
                datatype=["str", "number", "number"],
                col_count=(3, "fixed"),
                overflow_row_behaviour='paginate',
                max_rows=10,
                elem_id='dataframe'
            )

    gallery.select(get_select_index, None, selected)    
    btn.click(input_opt, 
              inputs=[folder, model_name, device_select], 
              outputs=[gallery, selected, tables]
            )

if __name__ == "__main__":
    demo.launch()