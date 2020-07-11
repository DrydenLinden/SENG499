# SENG499
The repository to hold the code for the SENG 499 Capstone Project.
https://github.com/marina-dunn/SENG499

face-recognition installation:
-Python3
-pip3
-cmake
-dlib

    apt-get update
    apt-get install build-essential cmake
    apt-get install libopenblas-dev liblapack-dev 
    apt-get install libx11-dev libgtk-3-dev
    apt-get install python python-dev python-pip
    apt-get install python3 python3-dev python3-pip
    
    Install dlib (can take some time to build)
    ------------------------------------------
    cd ~
    mkdir temp
    cd temp
    git clone https://github.com/davisking/dlib.git
    cd dlib
    mkdir build; cd build; cmake ..; cmake --build .
    cd ..
    python3 setup.py install
    
    face-recognition (will take some time to install)
    -------------------------------------------------
    pip3 install face_recognition
    
Potential libraries for machine learning:
-scikit-learn
-numpy 
-scipy 
-matplotlib 
-pandas

face_test.py
-sample code for face-recognition, outlines facial features of given image

proc_face.py
-given single image outputs csv with processed data points

gen_test_data.py
-given a directory of face images outputs proccessed data points for each

Processed data format:
sample number, facial feature, x:y, x:y, ...

Processed data points are currently relative to first data point (x0 - x:y0 - y). Some ideas for other point references, center of cluster (k-means), mean point.
Could also repfresent points at distance angle from a mean point (could perhaps identify convex or concave curve of mouth)


# Docker
docker compose can be used to launch the application
There are 2 volumes that are used for the application: input and output
These volumes allow the container to be run for testing without needing to rebuild it

1) Put files you want to analyze in the input folder
2) Run docker-compose up
3) Resulting data.csv file is put in output folder

When code is changed used docker-compose up --build