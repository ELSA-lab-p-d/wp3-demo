VERSION_NODE=3.7.3
VERSION_SERVER=$VERSION_NODE


pip install vantage6==$VERSION_NODE

# Technically this is not needed, but makes life more easy ;-)
docker pull harbor2.vantage6.ai/infrastructure/server:$VERSION_NODE
docker pull harbor2.vantage6.ai/infrastructure/node:$VERSION_NODE

########################
# Central server setup
########################

# Start server
cd infrastructure/server
server_config=$(pwd)/wp3server.yaml
vserver start --user -c $server_config --image harbor2.vantage6.ai/infrastructure/server:$VERSION_SERVER

# Import server entities
server_entities=$(pwd)/entities.yaml
vserver import --user -c $server_config $server_entities

cd ../../

########################
# InfoRing node setup
########################

cd infrastructure/inforing

# Generate random dataset
python prepare.py

# InfoRing node start
inforing_config=$(pwd)/inforing.yaml
vnode start --user -c $inforing_config --image harbor2.vantage6.ai/infrastructure/node:$VERSION_NODE

########################
# Launch user interface
########################
docker run --rm -d \
    --name vantage6-ui \
    -p 80:80 \
    -e "SERVER_URL=http://localhost:5000" \
    -e "API_PATH=/api" \
    ghcr.io/maastrichtu-biss/vantage6-ui:merged-dashboard
