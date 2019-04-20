# Flasky

*A simple REST service powered by Flask*

![Travis](https://img.shields.io/travis/gmarciani/flasky.svg?style=popout)
![Codecov](https://img.shields.io/codecov/c/github/gmarciani/flasky.svg?style=popout)
![Release](https://shields.beevelop.com/github/release/beevelop/docker-shields.svg?style=popout)
[![Docker Version](https://images.microbadger.com/badges/version/gmarciani/flasky.svg)](https://microbadger.com/images/gmarciani/flasky)
[![Docker Size](https://images.microbadger.com/badges/image/gmarciani/flasky.svg)](https://microbadger.com/images/gmarciani/flasky)
![License](https://img.shields.io/github/license/gmarciani/flasky.svg?style=popout)
![Gitter](https://img.shields.io/gitter/room/gmarciani/flasky.svg?color=37d3b4&style=popout)


### Docker
```
docker run -p 8000:8000 flasky
```

### Kubernetes

#### Minikube

Create the Deployment

```
kubectl apply -f kubernetes/flasky-deployment.yaml
```

Create the Service

```
kubectl apply -f kubernetes/flasky-service.yaml
```

Retrieve the Service URL

```
minikube service flasky-service --url
```


### Tests

Run all tests

```
pytest
```


### Stress Testing

Configure Locust stress tests

```
locust -f locust/locustfile.py --host ${FLASKY_SERVICE_URL_AND_PORT}
```

Run Locust stress tests on `http://127.0.0.1:8089/`


## Authors
Giacomo Marciani, [mgiacomo@amazon.com](mailto:mgiacomo@amazon.com)


## License
The project is released under the [MIT License](https://opensource.org/licenses/MIT).
