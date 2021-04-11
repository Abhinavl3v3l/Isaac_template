FROM firekind/isaac:2020.2

COPY requirements.txt /tmp

RUN python3 -m pip install -r /tmp/requirements.txt 