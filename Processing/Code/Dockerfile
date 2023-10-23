FROM condaforge/miniforge3
#
# "FSL development team <https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/>" created base docker container for single FSL functionalities
#
# FSL functionalities integrated here:
# flirt
# fsl-utils: fslstats
#
#
LABEL maintainer: "Patrik Bey, patrik.bey@bih-charite.de"
ENV PATH="/opt/conda/bin:${PATH}"

# install FSL functionalities from conda channel
ENV FSL_CONDA_CHANNEL="https://fsl.fmrib.ox.ac.uk/fsldownloads/fslconda/public"
RUN /opt/conda/bin/conda install -n base -c conda-forge tini
RUN /opt/conda/bin/conda install -n base -c $FSL_CONDA_CHANNEL fsl-flirt -c conda-forge
RUN /opt/conda/bin/conda install -n base -c $FSL_CONDA_CHANNEL fsl-utils -c conda-forge
# set FSLDIR so FSL tools can use it, in this minimal case, the FSLDIR will be the root conda directory
ENV FSLDIR="/opt/conda"
ENV FSLOUTPUTTYPE="NIFTI_GZ"

RUN mkdir "/opt/src"
COPY Code "/opt/src"
ENV SRCDIR="/opt/src"
# ENTRYPOINT [ "/opt/conda/bin/tini", "--", "/entrypoint" ]

