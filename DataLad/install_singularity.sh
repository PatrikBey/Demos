


# sudo apt-get update && sudo apt-get install -y \
#     build-essential \
#     libssl-dev \
#     uuid-dev \
#     libgpgme11-dev \
#     squashfs-tools \
#     libseccomp-dev \
#     pkg-config


# export VERSION=1.13.5 OS=linux ARCH=amd64 && \
#     wget https://dl.google.com/go/go$VERSION.$OS-$ARCH.tar.gz && \
#     sudo tar -C /usr/local -xzvf go$VERSION.$OS-$ARCH.tar.gz && \
#     rm go$VERSION.$OS-$ARCH.tar.gz


# echo 'export GOPATH=${HOME}/go' >> ~/.bashrc && \
#     echo 'export PATH=/usr/local/go/bin:${PATH}:${GOPATH}/bin' >> ~/.bashrc && \
#     source ~/.bashrc

# https://github.com/apptainer/singularity/releases/download/v3.5.3/singularity-3.5.3.tar.gz
# export VERSION=3.5.3 && # adjust this as necessary \
# wget https://github.com/apptainer/singularity/releases/download/v${VERSION}/singularity-${VERSION}.tar.gz && \
#     tar -xzf singularity-${VERSION}.tar.gz && \
#     cd singularity

#     # wget https://github.com/sylabs/singularity/releases/download/v${VERSION}/singularity-${VERSION}.tar.gz && \

# git clone https://github.com/sylabs/singularity.git && \
#     cd singularity && \
#     git checkout v3.5.3


# ./mconfig && \
#     make -C ./builddir && \
#     sudo make -C ./builddir install




sudo apt-get update && \
sudo apt-get install -y build-essential \
libseccomp-dev pkg-config squashfs-tools cryptsetup

sudo rm -r /usr/local/go

export VERSION=1.13.15 OS=linux ARCH=amd64  # change this as you need

wget -O /tmp/go${VERSION}.${OS}-${ARCH}.tar.gz https://dl.google.com/go/go${VERSION}.${OS}-${ARCH}.tar.gz && \
sudo tar -C /usr/local -xzf /tmp/go${VERSION}.${OS}-${ARCH}.tar.gz

echo 'export GOPATH=${HOME}/go' >> ~/.bashrc && \
echo 'export PATH=/usr/local/go/bin:${PATH}:${GOPATH}/bin' >> ~/.bashrc && \
source ~/.bashrc

curl -sfL https://install.goreleaser.com/github.com/golangci/golangci-lint.sh |
sh -s -- -b $(go env GOPATH)/bin v1.21.0

mkdir -p ${GOPATH}/src/github.com/sylabs && \
cd ${GOPATH}/src/github.com/sylabs && \
git clone https://github.com/sylabs/singularity.git && \
cd singularity

git checkout v3.6.3

cd ${GOPATH}/src/github.com/sylabs/singularity && \
./mconfig && \
cd ./builddir && \
make && \
sudo make install

singularity version