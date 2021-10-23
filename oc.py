import sys
arg = sys.argv

i = 1

def manual():
    sys.exit('''
python ocrhdr.py -t [Input Type] -f [File Type] [Path] -h [CPU/GPU] -o [Output Path]

[Input Type]:   H: Handwriten Digit
                T: Typed Text

[File Type]:    I: Image
                V: Video
                S: Screen
                C: Capture
''')

while i<len(arg):
    if arg[i] == '-t':
        # Check is it handwriten Digit or Typed  Text
        input_type = arg[i+1]
   
    elif arg[i] == '-f':
        file_type = arg[i+1]

        if file_type != 'S' or file_type != 'C':
            file_path = arg[i+2]
    
    elif arg[i] == '-h':
        hardware = arg[i+1]

    elif arg[i] == '-o':
        output_file = arg[i+1]
    
    elif arg[i] == '--help':
        manual()

    i+=1

def ImageToText(path):
    results = reader.readtext(path)

    for result in results[:-4]:
        top_left = result[0][0]
        bottom_right = result[0][2]
        text = result[1]
        print(text)
   
if input_type == 'H':
    pass

elif input_type == 'T':

    import easyocr
    import cv2
    from matplotlib import pyplot as plt
    import numpy as np

    if hardware == 'gpu':
        reader = easyocr.Reader(['en'],gpu=True)
    else:
        reader = easyocr.Reader(['en'],gpu=False)

    if file_type == 'I':
        ImageToText(file_path)
        sys.exit('Task Complete')

    elif file_type == 'S':
        import pyautogui
        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
        cv2.imwrite('Image.png',image)
        ImageToText('Image.png')

    elif file_type == 'V':
        cap = cv2.VideoCapture(path)
 
    elif file_type == 'C':
        cap = cv2.VideoCapture(0)

    while True:
        _, img = cap.read()
        if img is None:
            break

        img = cv2.resize(img, None, fx=0.4, fy=0.4)
        
        ImageToText(img)

