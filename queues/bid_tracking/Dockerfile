FROM python
WORKDIR /queues
COPY tracking.py .
RUN pip install pyzmq
CMD ["python", "tracking.py"]