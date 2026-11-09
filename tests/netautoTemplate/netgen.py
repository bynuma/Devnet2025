# netgen.py
from jinja2 import Template                         # The Template class is imported from the jinja2 module to create a Jinja2 template for generating network interface configuration. This class will be used to define a template string and render it with the provided interface data.

def generate_interface_config(interface_data):      # The generate_interface_config function is defined to generate a network interface configuration based on the provided interface_data dictionary. This function will use a Jinja2 template to create the configuration string.
    template_str = """
interface {{ name }}
 description {{ description }}
 ip address {{ ip_address }} {{ subnet_mask }}
 no shutdown
"""
    template = Template(template_str.strip())       # A Jinja2 Template object is created using the template_str defined above. The strip() method is called to remove any leading or trailing whitespace from the template string. This template will be used to generate the network interface configuration by replacing the placeholders with actual values from the interface_data dictionary.
    return template.render(interface_data)          # The render() method of the Template object is called with the interface_data dictionary as an argument. This method replaces the placeholders in the template with the corresponding values from the interface_data dictionary and returns the generated configuration string. The resulting configuration string is then returned by the generate_interface_config function.

###### NOTE #######
# The template string is defined using triple quotes ("""). This string contains the Jinja2 template for generating the network interface configuration. The template includes placeholders for the interface name, description, IP address, and subnet mask, which will be replaced with the actual values from the interface_data dictionary during rendering.
###################