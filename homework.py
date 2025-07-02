def unicorns_to_rainbows(unicorns: list[dict]) -> list[str]:
    rainbows = [f"🌈 Rainbow unicorn of color {i["color"]}" for i in unicorns]
    return rainbows

unicorns = [{"color": "pink"}, {"color": "blue"}, {"color": "sparkly"}]
print(unicorns_to_rainbows(unicorns))