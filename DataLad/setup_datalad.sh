
# Preparing datalad container workflow hands-on session for HBPSummit 2023

# https://handbook.datalad.org/en/latest/intro/installation.html

sudo apt-get install datalad

pip install datalad-container


git config --global --add user.name "Alan Turing"
git config --global --add user.email "alan@turing.machine"



# Path=/mnt/h/Research/Demos/DataLad
Path='/mnt/c/Users/me/Research/Data/Demo'


cp /mnt/c/Users/me/GitHub/Demos/ElevatedPlusMaze/Data/Data.txt $Path/Data.txt

cd $Path

datalad create -c text2git DataLad-Demo

mkdir DataLad-Demo/Data
cp /mnt/c/Users/me/GitHub/Demos/ElevatedPlusMaze/Data/Data.txt $Path/DataLad-Demo/Data/Data.txt

datalad save -m "include example data"

git log



datalad containers-add DataLad-demo --url docker://patrikneuro/epm:demo
# add container for epm

datalad save -m "include example container"



# run container via datalad
datalad containers-run 

datalad containers-run DataLad-demo

