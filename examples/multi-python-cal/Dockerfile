###########################################
# BASE IMAGE (Build Stage)
###########################################

FROM ubuntu AS build

RUN apt-get update && apt-get install -y python3 python3-pip

WORKDIR /app

COPY . . 

############################################
# MULTI-STAGE BUILD - FINAL IMAGE
############################################

FROM gcr.io/distroless/python3

# Set working directory
WORKDIR /app

# Copy only the necessary files from the build stage
COPY --from=build /app /app

# Set entrypoint for the Python application
ENTRYPOINT ["python3", "/app/calculator.py"]
