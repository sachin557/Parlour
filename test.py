import re
saloon_name="['Saloon A']"
up_saloon_name=re.sub(r"[^A-Z a-z]","",saloon_name)
print(up_saloon_name)
updated_saloon_name=up_saloon_name.replace(" ","+") if " " in up_saloon_name else up_saloon_name
print(updated_saloon_name)