from unicode import name
import yaml
import json

with open(r"input.json") as json_file:
    json_data = json.load(json_file)

with open(r"networkpolicy.yaml") as yaml_file:
    yaml_data_template = yaml.safe_load(yaml_file)

for namespace_name in json_data:
    new_yaml_data = dict(yaml_data_template)
    current_namespace = json_data[namespace_name]
    
    domains = current_namespace[0].split("/")
    ports = current_namespace[1].split("/")
    
    new_yaml_data['metadata']['namespace']= namespace_name
    new_yaml_data['spec']['egress']['destination']['domains']= domains 
    new_yaml_data['spec']['egress']['destination']['ports'] = ports
    
    new_yaml_data_text = yaml.safe_dump(new_yaml_data, allow_unicode=True)
    
    print(new_yaml_data_text)
