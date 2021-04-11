#!/bin/bash

NAME=isaac_application

docker container start -i $NAME || (printf "Creating new container...\n" && docker run --gpus all --net host --privileged -v `pwd`:/workspaces/isaac_application -w /workspaces/isaac_application --mount source=isaac-sdk-build-cache,target=/root --name $NAME -it firekind/isaac:2020.2 /bin/bash)
