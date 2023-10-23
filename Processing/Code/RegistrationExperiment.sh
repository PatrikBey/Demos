#!/bin/bash
#
# # RegistrationExperiment.sh
#
# * Brain Simulation Section
# * Charité Berlin Universitätsmedizin
# * Berlin Institute of Health
#
# ## Author(s)
# * Bey, Patrik, Charité Universitätsmedizin Berlin, Berlin Institute of Health
# 
#
# * last update: 2023.10.23
#
#
# This script is used to co-register a T1w input image into MNI template space
# and highlight the impact of interpolation variable on processin results.
#
#
#

#############################################
#                                           #
#           PREPARE CONTAINER               #
#                                           #
#############################################

# start interactive session of container including Data directory mounted as "/data"
# docker run -it -v ${PWD}/Data:/data demos:fsl bash

# call in single docker call
# docker run -v ${PWD}/Data:/data -v ${PWD}/Code:/code demos:fsl bash /code/RegistrationExperiment.sh



#################################################
#                                               #
#              CREATE VARIABLES                 #
#                                               #
#################################################


# define input image
Input="/data/input.nii.gz"

# define reference image
Reference="/data/MNI152_T1_2mm.nii.gz"

# define atlas in reference space
Atlas="/data/HCPMMP1_MNI152.nii.gz"

# define output filenames
OutputImage="/data/In2Ref.nii.gz"
OutputTransformation="/data/In2Ref.mat"

# get some general information about input images
echo "FSLINFO for Input varialble: "
fslinfo "${Input}"

echo "FSLINFO for Reference varialble: "
fslinfo "${Reference}"

echo "FSLINFO for Atlas varialble: "
fslinfo "${Atlas}"


# get familiar with linear co-registration function FSL-flirt
flirt


#################################################
#                                               #
#               DO COMPUTATIONS                 #
#                                               #
#################################################

echo "START:    co-registration experiment."


#---------STANNDARD SPACE COREGISTRATION--------#

echo "UPDATE:    registering input to MNI template with default parameters."
flirt \
    -in "${Input}" \
    -ref "${Reference}" \
    -omat "${OutputTransformation}" \
    -out "${OutputImage}"


#---------ADJUSTED INTERPOLATION METHOD--------#

# define output filenames
OutputImage="/data/In2Ref_NN.nii.gz"
OutputTransformation="/data/In2Ref_NN.mat"

echo "UPDATE:    registering input to MNI template with changed interpolations parameter."

flirt \
    -in "${Input}" \
    -ref "${Reference}" \
    -interp "nearestneighbour" \
    -omat "${OutputTransformation}" \
    -out "${OutputImage}"


#------DIFFERENCE IN INTERPOLATION METHOD------#

echo "UPDATE:    computing difference image between co-registration results."

fslmaths \
    "/data/In2Ref_NN.nii.gz" \
    -sub \
    "/data/In2Ref.nii.gz" -abs \
    "/data/RegistrationDifference.nii.gz"



#------INVERSE TRANSFORMATION DIRECTION------#

In2Ref="/data/In2Ref_NN.mat"
Ref2In="/data/Ref2In_NN.mat"

echo "UPDATE:    creating inverse transformation matrix."
convert_xfm \
    ${In2Ref} \
    -inverse \
    -omat "${Ref2In}"


# apply inverse transformation to Atlas
# from template space to subject space

Output="/data/HCPMMP1_subject.nii.gz"

echo "UPDATE:    applying inverse transformation to atlas image."
flirt \
    -applyxfm \
    -usesqform \
    -init "${Ref2In}" \
    -in "${Atlas}" \
    -ref "${Input}" \
    -out "${Output}"


echo "FINISHED:    co-registration experiment."
