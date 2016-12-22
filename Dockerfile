FROM gchiam/openjdk:8

RUN apk --update add \
    ca-certificates \
    bash \
    curl \
    build-base \
    gcc \
    python \
    python-dev \
    py-pip

RUN pip install -U pip

# install Pykafka and Tweepy
#RUN pip install pykafka
#RUN pip install tweepy

# download and install Leiningen
ENV LEIN_ROOT=1
RUN curl https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein > ./lein
RUN chmod a+x ./lein
RUN mv ./lein /usr/bin/lein
RUN lein version

# install Streamparse
RUN pip install streamparse

# organize and change working directory
#ADD . /collision_map
#WORKDIR /collision_map

# use `docker run --interactive` and get to terminal entry point
ENTRYPOINT ["/bin/bash"]
