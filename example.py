import minecraft_data
# Java edition minecraft-data
mcd = minecraft_data("1.20.1")

print(str(mcd.version) + "\n")

print(mcd.find_item_or_block(1))
print(str(mcd.find_item_or_block('stone')) + "\n")

print(str(mcd.recipes['5'][0]) + "\n")

print(str(mcd.windows['minecraft:brewing_stand']) + "\n")

print(str(mcd.effects_name['Haste']) + "\n")


# # Query common data. E.g. to map the protocol version to a minecraft version
# protocol_version = 754 # example protocol version
# for version in minecraft_data.common().protocolVersions:
#     if version["version"] == protocol_version:
#         print(version["minecraftVersion"]) # 1.16.5
#         break
