from string import Template
from datetime import datetime

with open('string_template/template.html') as html:
    template = Template(html.read())
    data = datetime.now().strftime('%d/%m/%Y')
    msg = template.substitute(name='Lara', date=data)
    
print(msg)