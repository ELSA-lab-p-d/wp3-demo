source ./venv/bin/activate
vnode stop --user -n inforing
vserver stop --user -n wp3server
deactivate

docker volume rm $(docker volume ls -f name=vantage6 -q)
# docker volume rm $(docker volume ls -f name=inforing -q)

docker network rm $(docker network ls -f name=vantage6 -q)

# Optional: delete images
# docker rmi -f $(docker image ls --filter=reference='harbor*/*/*' -q)

rm -R ~/Library/Application\ Support/vantage6/node/inforing
rm -R ~/Library/Application\ Support/vantage6/server/wp3server