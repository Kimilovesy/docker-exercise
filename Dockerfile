# We tell docker to use a base image from https://hub.docker.com/_/python/
# We pick a GNU/Linux distribution (debian) which ships with python installed
FROM python:3.8

ENV USERNAME=myuser
ENV UID=1000
ENV GID=100

#
RUN useradd -m -s /bin/bash -N -u ${UID} ${USERNAME}
RUN pip install jupyter_dashboards pandas dash plotly pyarrow
RUN jupyter dashboards quick-setup --sys-prefix

USER ${USERNAME}
WORKDIR /home/${USERNAME}
# At build time we copy the py file  from our host to the image
COPY app_barplot.py .
COPY app_histogram.py .

# At run time hello.py is executed inside the container
CMD ["python", "app_barplot.py"]
