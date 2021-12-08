FROM python:3.9.9-bullseye
LABEL maintainer="dev.scholz@mailbox.org"

WORKDIR /src

RUN apt-get -qq update
RUN apt-get -qq install -y apt-utils
RUN apt-get -qq install -y build-essential
RUN apt-get -qq install -y bison
RUN apt-get -qq install -y swig
RUN apt-get -qq install -y libasound2-dev
RUN apt-get -qq install -y libpulse-dev
RUN apt-get -qq install -y ffmpeg

RUN git clone https://github.com/cmusphinx/sphinxbase.git
WORKDIR /src/sphinxbase
RUN ./autogen.sh
RUN ./configure
RUN make
RUN make install
WORKDIR /src


RUN git clone https://github.com/cmusphinx/pocketsphinx.git
WORKDIR /src/pocketsphinx
RUN ./autogen.sh
RUN ./configure
RUN make
RUN make install
WORKDIR /src

RUN pip install poetry
RUN git clone https://github.com/sims1253/voicemage.git
WORKDIR /src/voicemage


RUN poetry install
WORKDIR /src/voicemage/voicemage

RUN poetry run python model_setup.py
ADD run.sh /
RUN chmod +x /run.sh

