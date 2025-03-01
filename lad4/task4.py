import json

with open("lad4/sample-data.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 65)
print(f"{'DN':<55} {'Description':<15} {'Speed':<7} {'MTU'}")
print("-" * 65)

for item in data["imdata"]:
    interface = item["l1PhysIf"]["attributes"]
    print(f"{interface['dn']:<55} {interface.get('descr', ''):<15} {interface['speed']:<7} {interface['mtu']}")  
