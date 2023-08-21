with open("requirements.txt", "r") as file:
    lines = file.readlines()

package_names = []

for line in lines:
    package_name = line.split("==")[0].split("[")[0].strip()
    if package_name:
        package_names.append(package_name)

print(package_names)