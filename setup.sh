VERSION_NODE=3.10.4
VERSION_SERVER=$VERSION_NODE

python -m venv ./venv
source ./venv/bin/activate

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

# InfoRing node start
cd infrastructure/inforing
inforing_config=$(pwd)/inforing.yaml
vnode start --user -c $inforing_config --image harbor2.vantage6.ai/infrastructure/node:$VERSION_NODE