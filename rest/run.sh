docker build -t bid-capture-service -f ./capture/dockerfile ./capture/
docker build -t bid-tracking-service -f ./tracking/dockerfile ./tracking/
docker build -t bid-analytics-service -f ./analytics/dockerfile ./analytics/

docker build -t bid-producer-service -f ./producer/dockerfile ./producer/

docker-compose up --build