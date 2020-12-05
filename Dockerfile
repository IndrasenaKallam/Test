#################################################
# Build custom agent
################################################

FROM centos:latest

USER root

# copy the requirement.txt to docker images

COPY  /home/ec2-user/test/requirements.txt /tmp/

# installing the required packages

RUN yum clean all && \
	yum install -y python38 && \
	yum install -y python38-devel && \
	yum install -y libffi-devel && \
	yum install -y libffi-devel && \
	yum install -y gcc && \
	yum clean all

# make sure that the tools have been installled correctly
RUN python3 --version

# Try to reduce the size of docker image
RUN yum clean all && rm -rf /var/cache/yum

# vaas user config
RUN adduser -c "service account user" vaas
RUN ls /etc/
RUN mkdir /etc/sudoers.d
RUN ls /etc/sudoers.d
RUN touch /etc/sudoers.d/vaas
RUN echo "vaas ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/vaas && chmod 0440 /etc/sudoers.d/vaas

CMD ["bash"]
