FROM continuumio/miniconda3

# Metadata
LABEL maintainer="you@example.com"

# Set working directory
WORKDIR /app

# Copy everything
COPY . /app

# Install dependencies via conda
RUN conda update -n base -c defaults conda && \
    conda create -n molenv python=3.9 -y && \
    echo "conda activate molenv" >> ~/.bashrc

# Activate environment and install packages
SHELL ["conda", "run", "-n", "molenv", "/bin/bash", "-c"]

RUN conda install -c conda-forge rdkit -y && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose Flask port
EXPOSE 5000

# Run the app
CMD ["conda", "run", "--no-capture-output", "-n", "molenv", "python", "app.py"]
