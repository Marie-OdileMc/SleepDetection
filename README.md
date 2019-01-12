# SleepDetection
EPF school project for sleep detection with a reactivity test

# Installation

In order to use this project you will need to install OpenCV, Dlib and Python
To do this use the following links :

- https://www.learnopencv.com/install-opencv3-on-windows/
- https://www.learnopencv.com/install-opencv-3-and-dlib-on-windows-python-only/

But also the following libs (using pip) :
- scipy 
- numpy 
- imutils 

Clone the code from github:

```
git clone https://github.com/Marie-OdileMc/SleepDetection.git
```

Build the main dlib library:

```
cd dlib
mkdir build; cd build; cmake .. -DDLIB_USE_CUDA=0 -DUSE_AVX_INSTRUCTIONS=1; cmake --build .
```

Build and install the Python extensions:

```
cd ..
python3 setup.py install --yes USE_AVX_INSTRUCTIONS --no DLIB_USE_CUDA
```
 
Also you will need dlib’s pre-trained facial landmark detector that you can download from here "http://jmp.sh/4bIYiPU ". Place it at the root of your folder (where the two python files will be)
