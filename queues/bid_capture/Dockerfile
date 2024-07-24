FROM python
WORKDIR /queues
COPY capture.py .
RUN pip install pyzmq
CMD ["python", "capture.py"]