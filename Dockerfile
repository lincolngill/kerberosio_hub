FROM python:3-slim
WORKDIR /camviewer
# Copy the current directory contents into the container at /app
ADD . /camviewer
RUN pip install -r requirements.txt
EXPOSE 8080
# Define environment variable
ENV NAME World
CMD ["python", "CamViewer.py"]