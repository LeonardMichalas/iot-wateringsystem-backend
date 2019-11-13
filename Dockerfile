FROM golang:latest 

RUN mkdir /app 

ADD . /app/ 

WORKDIR /app 

RUN go get github.com/gorilla/mux

RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o /app/main .

FROM scratch
COPY --from=0 /app/main /app/main
ENTRYPOINT ["/app/main"]
