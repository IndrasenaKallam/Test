#################################################
# Build custom agent
################################################

FROM centos:latest

USER root

# copy the requirement.txt to docker images

COPY  ./*requirements.txt /test/
COPY ./test.py /test/


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

# indra user config
RUN adduser -c "account-user" indra
RUN ls /etc/
RUN mkdir /etc/sudoers.d
RUN ls /etc/sudoers.d
RUN touch /etc/sudoers.d/indra
RUN echo "indra ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/indra && chmod 0440 /etc/sudoers.d/indra

CMD ["bash"]
