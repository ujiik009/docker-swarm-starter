
### Docker swarm mode command

// master 
docker swarm init --advertise-addr <IP>

// worker
docker swarm join --token <TOKEN>

### Start Service in Swarm
```
docker stack deploy --compose-file docker-stack.yml starter
```
### List of Service in stack
```
docker stack services starter
```

App running at: http://127.0.0.1:8080