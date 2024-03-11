def heading_generator (title, type_heading):
    return f'<h{type_heading}>{title}</h{type_heading}>'

print(heading_generator('hola johan', '1'))