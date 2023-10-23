




# adjust for demos:fsl container name
docker run -it ale:dev bash



#################################################
#                                               #
#              CREATE VARIABLES                 #
#                                               #
#################################################


# define input image
Input="/data/input.nii.gz"

# define reference image
Reference="/data/MNI.nii.gz"

# define atlas in reference space
Atlas="/data/HCPMMP1.nii.gz"

# defie output filenames

OutputImage="/data/In2Ref.nii.gz"
OutputTransformation="/data/In2Ref.mat"

# get some general information about input images

fslinfo ${Input}
fslinfo ${Reference}
fslinfo ${Atlas}


# get familiar with linear co-registration function FSL-flirt
flirt


#################################################
#                                               #
#               DO COMPUTATIONS                 #
#                                               #
#################################################


flirt \
    -in ${Input} \
    -ref ${Reference} \
    -omat ${OutputTransformation} \
    -out ${OutputImage}


# create atlas in subject space
# 

flirt \
    -applyxfm \
    
