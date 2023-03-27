
# Preparing datalad container workflow hands-on session for HBPSummit 2023

# https://handbook.datalad.org/en/latest/intro/installation.html

sudo apt-get install datalad

pip install datalad-container


git config --global --add user.name "Alan Turing"
git config --global --add user.email "alan@turing.machine"



# Path=/mnt/h/Research/Demos/DataLad
Path='/mnt/c/Users/me/Research/Data/Demo'
cd $Path

datalad create -c text2git DataLad-Demo

cd DataLat-Demo

mkdir Data
cd Data

wget https://github.com/PatrikBey/Demos/blob/main/ElevatedPlusMaze/Data/Data.txt 

datalad save -m "include example data"

git log


# add container for epm from docker hub
datalad containers-add DataLad-demo --url docker://patrikneuro/epm:demo


# run container via singularity
singularity run --bind $PWD/Data:/data .datalad/environments/DataLad-Demo/image 


datalad save -m "singularity plotting"


# run container via datalad
# datalad containers-run -n DataLad-demo -i $PWD/Data:/data -o . "python /src/RUN.py --filename=$PWD/Data/Data.txt"



