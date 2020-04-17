FROM python:3-slim
WORKDIR /src
# Copy the current directory contents into the container at /app
ADD ./src /src
RUN pip install -r requirements.txt
EXPOSE 8080
# Define environment variable
ENV FLASK_DEBUG=N
CMD ["python", "run_khub.py"]