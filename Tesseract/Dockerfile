# Use an official Ubuntu runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# # Create a non-privileged user that the app will run under.
# # See https://docs.docker.com/go/dockerfile-user-best-practices/
# ARG UID=10001
# RUN adduser \
#     --disabled-password \
#     --gecos "" \
#     --home "/nonexistent" \
#     --shell "/sbin/nologin" \
#     --no-create-home \
#     --uid "${UID}" \
#     appuser
# USER appuser

# Install Python, Tesseract OCR and its dependencies
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev
    # tesseract-ocr-eng \
    # && apt-get clean \
    # && rm -rf /var/lib/apt/lists/*

RUN pip3 install -r requirements.txt

# Verify Tesseract installation
RUN tesseract --version

# Set the command to run when the container starts
CMD ["streamlit", "run", "streamlit.py"]