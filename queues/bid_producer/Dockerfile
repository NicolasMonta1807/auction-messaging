FROM python
WORKDIR /queues
COPY producer.py .
RUN pip install pyzmq
CMD ["python", "producer.py"]
