import yaml
import json

NAMESPACE = "${namespace}"
DOMAIN_NAME_1 = "${Domain_1}"
PORT_1 = "${Port_1}"

with open(r"input.json") as json_file:
    json_data = json.load(json_file)

with open(r"networkpolicy.yaml") as yaml_file:
    yaml_data_template = yaml.safe_load(yaml_file)

for namespace_name in json_data:
    new_yaml_data = dict(yaml_data_template)
    current_namespace = json_data[namespace_name]
    domain = current_namespace['domain']
    port = current_namespace['port']
    new_yaml_data['metadata']['namespace']= namespace_name
    new_yaml_data['spec']['egress'][0]['destination']['domains'][0] = domain 
    new_yaml_data['spec']['egress'][0]['destination']['ports'][0] = port
    new_yaml_data_text = yaml.dump(new_yaml_data)
    
    print(new_yaml_data_text)